from typing import Optional

from growth.core.application import handlers
from growth.core.application.message_bus import (
    CommandHandlerMap,
    EventHandlerMap,
    MessageBus,
)
from growth.core.application.ports import IMessageBus, IUnitOfWork
from growth.core.application.unit_of_work import UnitOfWork
from growth.settings import Settings


def bootstrap(
    uow: Optional[IUnitOfWork] = None,
    settings: Optional[Settings] = None,
    command_handlers: Optional[CommandHandlerMap] = None,
    event_handlers: Optional[EventHandlerMap] = None,
) -> IMessageBus:
    if settings is None:
        settings = Settings()

    if uow is None:
        uow = UnitOfWork(settings=settings)

    if command_handlers is None:
        command_handlers = handlers.COMMAND_HANDLERS

    if event_handlers is None:
        event_handlers = handlers.EVENT_HANDLERS

    return MessageBus(
        uow=uow,
        command_handlers=command_handlers,
        event_handlers=event_handlers,
    )
