import typing
from typing import Protocol

from sqlalchemy.orm import Session

from growth.core.domain.commands import Command
from growth.core.domain.events import Event

Message = typing.Union[
    Command,
    Event,
]


class IInbox(typing.Protocol):
    def invoke(self, command: Command):
        ...


class IOutbox(typing.Protocol):
    def publish(self, event: Event):
        ...


class IMessageBus(IInbox, IOutbox):
    ...


class IUnitOfWork(Protocol):
    session: Session
    # Constraint: shouldn't expose SqlAlchemy Session on interface
    # However, use cases need session (for demo), would need DI in adapters

    def __enter__(self) -> "IUnitOfWork":
        ...

    def __exit__(self, *args):
        ...

    def is_active(self) -> bool:
        ...

    def commit(self):
        ...

    def rollback(self):
        ...
