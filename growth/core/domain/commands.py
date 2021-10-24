import abc
import decimal

from pydantic import BaseModel

from growth.core.domain import types


class Command(BaseModel, abc.ABC):
    ...


class ChangeMarketGrowthMargin(Command):
    market: types.Market
    margin: types.Rate


class ChangeMarketWholesaleCost(Command):
    market: types.Market
    price_per_unit: types.Rate


class ChangeMarketVariableRate(Command):
    market: types.Market
    price_per_unit: types.Rate


class ChangeTariffMarketVariableRate(Command):
    tariff_id: types.TariffId
    market: types.Market
    price_per_unit: types.Rate


class CalculateIncumbentRates(Command):
    market: types.Market


class CalculateSavings(Command):
    market: types.Market
