import time

from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events
from growth.core.domain.functions import do_some_work


def handle(session: Session, outbox: IOutbox, cmd: commands.ChangeMarketGrowthMargin):
    """
    Use case: Change growth margin
    Steps:
    - retrieve market
    - change growth margin
    - publish event
    """
    do_some_work()
    event = events.MarketGrowthMarginChanged(market=cmd.market, margin=cmd.margin)
    outbox.publish(event)
