from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketVariableRate):
    # retrieve market variable rate
    # compute new market variable rate
    # publish event
    event = events.MarketVariableRateChanged
