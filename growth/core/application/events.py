import decimal

from growth.core.application.ports import Event
from growth.core.domain import types


class MarketGrowthMarginChanged(Event):
    market: types.Market
    region_code: str
    margin: decimal.Decimal


class MarketWholesaleCostChanged(Event):
    market: types.Market
    region_code: str
    price_per_unit: types.Rate


class MarketVariableRateChanged(Event):
    market: types.Market
    region_code: str
    price_per_unit: types.Rate


class TariffMarketVariableRateChanged(Event):
    tariff_id: types.TariffId
    market: types.Market
    price_per_unit: types.Rate


class IncumbentRatesCalculated(Event):
    market: types.Market


class SavingsCalculated(Event):
    market: types.Market
