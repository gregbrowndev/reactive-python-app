import time

from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events


def handle(session: Session, outbox: IOutbox, cmd: commands.CalculateIncumbentRates):
    """
    Use case: Calculate Incumbent Rates
    Steps:
    - retrieve incumbents
    - change growth margin
    - publish event
    """
    time.sleep(2)
    event = events.IncumbentRatesCalculated(market=cmd.market)
    outbox.publish(event)
