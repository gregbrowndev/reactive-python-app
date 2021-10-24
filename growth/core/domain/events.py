import abc
import decimal

from pydantic import BaseModel

from growth.core.domain import types


class Event(BaseModel, abc.ABC):
    ...


class MarketGrowthMarginChanged(Event):
    market: types.Market
    margin: types.Rate


class MarketWholesaleCostChanged(Event):
    market: types.Market
    price_per_unit: types.Rate


class MarketVariableRateChanged(Event):
    market: types.Market
    price_per_unit: types.Rate


class TariffMarketVariableRateChanged(Event):
    tariff_id: types.TariffId
    market: types.Market
    price_per_unit: types.Rate


class IncumbentRatesCalculated(Event):
    market: types.Market


class SavingsCalculated(Event):
    market: types.Market
