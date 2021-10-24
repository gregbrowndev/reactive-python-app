from typing import Optional

from growth.core.application import handlers
from growth.core.application.message_bus import MessageBus
from growth.core.application.ports import IMessageBus, IUnitOfWork
from growth.core.application.unit_of_work import UnitOfWork
from growth.settings import Settings


def bootstrap(
    uow: Optional[IUnitOfWork] = None,
    settings: Optional[Settings] = None,
) -> IMessageBus:
    if settings is None:
        settings = Settings()

    if uow is None:
        uow = UnitOfWork(settings=settings)

    return MessageBus(
        uow=uow,
        command_handlers=handlers.COMMAND_HANDLERS,
        event_handlers=handlers.EVENT_HANDLERS,
    )
