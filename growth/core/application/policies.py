from growth.core.application import commands, events


def handle_market_growth_margin_changed(
    session, event: events.MarketGrowthMarginChanged
):
    command = commands.ChangeMarketVariableRate
    # dispatch command


def handle_market_wholesale_cost_changed(
    session, event: events.MarketWholesaleCostChanged
):
    command = commands.ChangeMarketVariableRate
    # dispatch command


def handle_market_variable_rate_changed(
    session, event: events.MarketVariableRateChanged
):
    command = commands.ChangeTariffMarketVariableRate
    # dispatch command


def handle_tariff_market_variable_rate_changed(
    session, event: events.TariffMarketVariableRateChanged
):
    command = commands.CalculateIncumbentRates
    # dispatch command


def handle_incumbent_rates_calculated(session, event: events.IncumbentRatesCalculated):
    command = commands.CalculateSavings
    # dispatch command
