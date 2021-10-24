import datetime
import decimal
import enum
import typing
import uuid

from pydantic import BaseModel


@enum.unique
class Territory(enum.Enum):
    ES = "ES"
    FR = "FR"
    TX = "TX"


@enum.unique
class Currency(enum.Enum):
    GBP = "GBP"
    EUR = "EUR"
    USD = "USD"

    @property
    def symbol(self):
        return {Currency.GBP: "£", Currency.EUR: "€", Currency.USD: "$"}[self]


@enum.unique
class Utility(enum.Enum):
    GAS = "G"
    ELECTRICITY = "E"


@enum.unique
class MarketType(enum.Enum):
    RESIDENTIAL = "RESIDENTIAL"


class Money(BaseModel):
    amount: datetime.datetime
    currency: Currency


class Market(BaseModel):
    territory: Territory
    region_code: typing.Optional[str]
    utility: Utility
    market_type: MarketType


class Rate(BaseModel):
    price_per_unit: decimal.Decimal
    effective_date: datetime.datetime


TariffId = typing.NewType("TariffId", uuid.UUID)
