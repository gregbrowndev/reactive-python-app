import decimal

from growth.core.application.ports import Command
from growth.core.domain import types


class ChangeMarketGrowthMargin(Command):
    market: types.Market
    region_code: str
    margin: decimal.Decimal


class ChangeMarketWholesaleCost(Command):
    market: types.Market
    region_code: str
    price_per_unit: types.Rate


class ChangeMarketVariableRate(Command):
    market: types.Market
    region_code: str
    price_per_unit: types.Rate


class ChangeTariffMarketVariableRate(Command):
    tariff_id: types.TariffId
    market: types.Market
    price_per_unit: types.Rate


class CalculateIncumbentRates(Command):
    market: types.Market


class CalculateSavings(Command):
    market: types.Market
