import logging
import typing
from dataclasses import dataclass

from pydantic import validate_arguments
from sqlalchemy.orm import Session

from growth.core.application import ports
from growth.core.application.ports import Command, Event, IInbox, IMessageBus, IOutbox

C = typing.TypeVar("C", bound=Command)
CommandHandler = typing.Callable[[Session, IOutbox, C], None]
CommandHandlerMap = typing.Dict[typing.Type[C], CommandHandler[C]]

E = typing.TypeVar("E", bound=Event)
EventHandler = typing.Callable[[Session, IInbox, E], None]
EventHandlerMap = typing.Dict[typing.Type[E], typing.List[EventHandler[E]]]


logger = logging.getLogger(__name__)


@dataclass
class MessageBus(IMessageBus, IInbox, IOutbox):
    session: Session
    event_handlers: EventHandlerMap
    command_handlers: CommandHandlerMap

    @validate_arguments
    def issue(self, command: ports.Command) -> ports.Event:
        self.queue: typing.List[ports.Message] = [command]
        self.responses: typing.List[ports.Event] = []

        # TODO
        #  - add session transaction management

        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, ports.Event):
                self._handle_event(message)
                self.responses.append(message)
            elif isinstance(message, ports.Command):
                self._handle_command(message)
            else:
                raise Exception(f"{message!r} was not an Event or Command")
        return self.responses[0]

    # TODO - create a nicer set of interfaces that handles transaction
    #  management transparently

    def invoke(self, command: Command):
        # Injected into each policy to publish commands onto the message
        # bus without starting a new unit of work
        self.queue.append(command)

    def publish(self, event: Event):
        # Injected into each use case to publish event onto the message
        # bus without starting a new unit of work
        self.queue.append(event)

    def _handle_command(self, command: ports.Command):
        logger.debug(f"handling command: {command!r}")
        try:
            # TODO - add tenacity retry
            handler = self.command_handlers[type(command)]
            handler(self.session, self, command)
        except Exception:
            logger.exception(f"Exception handling command: {command!r}")
            raise

    def _handle_event(self, event: ports.Event) -> None:
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug(f"handling event {event!r} with handler {handler!r}")
                handler(self.session, self, event)
            except Exception:
                logger.exception(f"Exception handling event: {event:!r}")
                continue
