from growth.core.application.message_bus import CommandHandlerMap, EventHandlerMap
from growth.core.application.policies import (
    handle_incumbent_rates_calculated,
    handle_market_growth_margin_changed,
    handle_market_variable_rate_changed,
    handle_market_wholesale_cost_changed,
    handle_tariff_market_variable_rate_changed,
)
from growth.core.application.usecases import (
    calculate_incumbent_rates,
    calculate_savings,
    change_growth_margin,
    change_market_variable_rate,
    change_market_wholesale_cost,
    change_tariff_market_variable_rate,
)
from growth.core.domain import commands, events

COMMAND_HANDLERS: CommandHandlerMap = {
    commands.ChangeMarketGrowthMargin: change_growth_margin.handle,
    commands.ChangeMarketWholesaleCost: change_market_wholesale_cost.handle,
    commands.ChangeMarketVariableRate: change_market_variable_rate.handle,
    commands.ChangeTariffMarketVariableRate: change_tariff_market_variable_rate.handle,
    commands.CalculateIncumbentRates: calculate_incumbent_rates.handle,
    commands.CalculateSavings: calculate_savings.handle,
}

EVENT_HANDLERS: EventHandlerMap = {
    events.MarketGrowthMarginChanged: [handle_market_growth_margin_changed],
    events.MarketWholesaleCostChanged: [handle_market_wholesale_cost_changed],
    events.MarketVariableRateChanged: [handle_market_variable_rate_changed],
    events.TariffMarketVariableRateChanged: [
        handle_tariff_market_variable_rate_changed
    ],
    events.IncumbentRatesCalculated: [handle_incumbent_rates_calculated],
    events.SavingsCalculated: [],
}
