import time

from sqlalchemy.orm import Session

from growth.core.application import commands, events
from growth.core.application.ports import IOutbox


def handle(session: Session, outbox: IOutbox, cmd: commands.ChangeMarketWholesaleCost):
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
    outbox.publish(event)
