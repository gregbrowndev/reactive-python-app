import typing

from growth.core.application.commands import *
from growth.core.application.events import *

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
