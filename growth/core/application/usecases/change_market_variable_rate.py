import time

from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events


def handle(session: Session, outbox: IOutbox, cmd: commands.ChangeMarketVariableRate):
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
    outbox.publish(event)
