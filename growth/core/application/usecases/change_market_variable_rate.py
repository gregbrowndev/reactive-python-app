import time

from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketVariableRate):
    """
    Use case: Change market variable rate
    Steps:
    - retrieve market variable rate
    - compute new market variable rate
    - publish event
    """
    time.sleep(2)
    event = events.MarketVariableRateChanged(
        market=cmd.market,
        region_code=cmd.region_code,
        price_per_unit=cmd.price_per_unit,
    )
