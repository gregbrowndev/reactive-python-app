from growth.core.application import commands, events


def change_market_variable_rate(session, cmd: commands.ChangeTariffMarketVariableRate):
    # retrieve tariff
    # set current market varible rate
    # publish event
    event = events.TariffMarketVariableRateChanged
