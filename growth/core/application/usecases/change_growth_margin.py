import time

from sqlalchemy.orm import Session

from growth.core.application import commands, events
from growth.core.application.ports import IOutbox


def handle(session: Session, outbox: IOutbox, cmd: commands.ChangeMarketGrowthMargin):
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
    outbox.publish(event)
