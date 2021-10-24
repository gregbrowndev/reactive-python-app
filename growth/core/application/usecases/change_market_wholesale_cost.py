from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketWholesaleCost):
    # retrieve market
    # change wholesale cost
    # publish event
    event = events.MarketWholesaleCostChanged
