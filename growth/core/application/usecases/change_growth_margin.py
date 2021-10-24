import time

from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeMarketGrowthMargin):
    """
    Use case: Change growth margin
    Steps:
    - retrieve market
    - change growth margin
    - publish event
    """
    time.sleep(2)
    event = events.MarketGrowthMarginChanged(
        market=cmd.market, region_code=cmd.region_code, margin=cmd.margin
    )
