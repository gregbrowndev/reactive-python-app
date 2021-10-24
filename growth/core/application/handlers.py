import typing

from growth.core.application import commands
from growth.core.application.ports import Command, CommandHandler, Event, EventHandler
from growth.core.application.usecases import (
    calculate_incumbent_rates,
    calculate_savings,
    change_growth_margin,
    change_market_variable_rate,
    change_market_wholesale_cost,
    change_tariff_market_variable_rate,
)

C = typing.TypeVar("C", bound=Command)
E = typing.TypeVar("E", bound=Event)
CommandHandlerMap = typing.Dict[typing.Type[C], CommandHandler[C]]
EventHandlerMap = typing.Dict[typing.Type[E], EventHandler[E]]


EVENT_HANDLERS: EventHandlerMap = {}

COMMAND_HANDLERS: CommandHandlerMap = {
    commands.ChangeMarketGrowthMargin: change_growth_margin.handle,
    commands.ChangeMarketWholesaleCost: change_market_wholesale_cost.handle,
    commands.ChangeMarketVariableRate: change_market_variable_rate.handle,
    commands.ChangeTariffMarketVariableRate: change_tariff_market_variable_rate.handle,
    commands.CalculateIncumbentRates: calculate_incumbent_rates.handle,
    commands.CalculateSavings: calculate_savings.handle,
}
