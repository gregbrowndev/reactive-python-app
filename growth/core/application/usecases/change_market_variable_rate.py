import time

from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events
from growth.core.domain.functions import do_some_work


def handle(session: Session, outbox: IOutbox, cmd: commands.ChangeMarketVariableRate):
    """
    Use case: Change market variable rate
    Steps:
    - retrieve market variable rate
    - compute new market variable rate
    - publish event
    """
    do_some_work()
    event = events.MarketVariableRateChanged(
        market=cmd.market,
        price_per_unit=cmd.price_per_unit,
    )
    outbox.publish(event)
