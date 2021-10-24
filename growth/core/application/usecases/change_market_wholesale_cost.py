import time

from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketWholesaleCost):
    """
    Use case: Change market wholesale cost
    - retrieve market
    - change wholesale cost
    - publish event
    """
    time.sleep(2)
    event = events.MarketWholesaleCostChanged(
        market=cmd.market,
        region_code=cmd.region_code,
        price_per_unit=cmd.price_per_unit,
    )
