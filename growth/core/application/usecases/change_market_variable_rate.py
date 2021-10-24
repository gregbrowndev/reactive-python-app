from growth.core.application import commands, events


def change_market_variable_rate(session, cmd: commands.ChangeMarketVariableRate):
    # retrieve market variable rate
    # compute new market variable rate
    # publish event
    event = events.MarketVariableRateChanged
