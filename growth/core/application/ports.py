import abc
from typing import Union

from pydantic import BaseModel


class Event(BaseModel, abc.ABC):
    ...


class Command(BaseModel, abc.ABC):
    ...


Message = Union[
    Command,
    Event,
]
