from growth.core.application import commands, events


def change_growth_margin(session, cmd: commands.ChangeMarketGrowthMargin):
    # retrieve growth margin state
    # change growth margin
    # publish event
    event = events.MarketGrowthMarginChanged
