from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketGrowthMargin):
    # retrieve market
    # change growth margin
    # publish event
    event = events.MarketGrowthMarginChanged
