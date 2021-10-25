import logging
import typing

from pydantic import validate_arguments
from sqlalchemy.orm import Session

from growth.core.application import ports
from growth.core.application.ports import (
    Command,
    Event,
    IInbox,
    IMessageBus,
    IOutbox,
    IUnitOfWork,
)

C = typing.TypeVar("C", bound=Command)
CommandHandler = typing.Callable[[Session, IOutbox, C], None]
CommandHandlerMap = typing.Dict[typing.Type[C], CommandHandler[C]]

E = typing.TypeVar("E", bound=Event)
EventHandler = typing.Callable[[Session, IInbox, E], None]
EventHandlerMap = typing.Dict[typing.Type[E], typing.List[EventHandler[E]]]


logger = logging.getLogger(__name__)


class MessageBus(IMessageBus, IInbox, IOutbox):
    uow: IUnitOfWork
    event_handlers: EventHandlerMap
    command_handlers: CommandHandlerMap

    def __init__(
        self,
        uow: IUnitOfWork,
        event_handlers: EventHandlerMap,
        command_handlers: CommandHandlerMap,
    ):
        self.uow = uow
        self.command_handlers = command_handlers
        self.event_handlers = event_handlers

    @validate_arguments
    def invoke(self, command: Command) -> typing.Optional[typing.List[ports.Event]]:
        # TODO - need to have separate interfaces for shell/core
        # Injected into each policy to publish commands onto the message
        # bus without starting a new unit of work
        if not self.uow.is_active():
            return self._start(command)
        self.queue.append(command)
        return None

    @validate_arguments
    def publish(self, event: Event):
        # Injected into each use case to publish events onto the message
        # bus without starting a new unit of work
        if not self.uow.is_active():
            return self._start(event)
        self.queue.append(event)

    def _start(self, message: ports.Message):
        with self.uow:
            self.queue: typing.List[ports.Message] = [message]
            self.responses: typing.List[ports.Event] = []
            while self.queue:
                message = self.queue.pop(0)
                if isinstance(message, ports.Event):
                    self._handle_event(message)
                    self.responses.append(message)
                elif isinstance(message, ports.Command):
                    self._handle_command(message)
                else:
                    raise Exception(f"{message!r} was not an Event or Command")
            self.uow.commit()
            return self.responses

    def _handle_command(self, command: ports.Command):
        try:
            logger.debug(f"handling command: {command!r}")
            # TODO - add tenacity retry
            # TODO - add transactional inbox
            handler = self.command_handlers[type(command)]
            handler(self.uow.session, self, command)
        except Exception:
            logger.exception(f"Exception handling command: {command!r}")
            raise

    def _handle_event(self, event: ports.Event) -> None:
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug(f"handling event {event!r} with handler {handler!r}")
                # TODO - add transaction outbox
                handler(self.uow.session, self, event)
            except Exception:
                logger.exception(f"Exception handling event: {event:!r}")
                continue
