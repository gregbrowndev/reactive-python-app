import abc
import typing

from pydantic import BaseModel


class Event(BaseModel, abc.ABC):
    ...


class Command(BaseModel, abc.ABC):
    ...


Message = typing.Union[
    Command,
    Event,
]

Session = typing.NewType("Session", dict)

C = typing.TypeVar("C", bound=Command)
E = typing.TypeVar("E", bound=Event)

CommandHandler = typing.Callable[[Session, C], None]
EventHandler = typing.Callable[[Session, E], None]
