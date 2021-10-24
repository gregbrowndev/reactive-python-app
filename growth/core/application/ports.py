import typing

from growth.core.domain.commands import Command
from growth.core.domain.events import Event

Message = typing.Union[
    Command,
    Event,
]


class IMessageBus(typing.Protocol):
    def issue(self, command: Command):
        ...


class IInbox(typing.Protocol):
    def invoke(self, command: Command):
        ...


class IOutbox(typing.Protocol):
    def publish(self, event: Event):
        ...
