from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events
from growth.core.domain.functions import do_some_work


def handle(session: Session, outbox: IOutbox, cmd: commands.CalculateIncumbentRates):
    """
    Use case: Calculate Incumbent Rates
    Steps:
    - retrieve incumbents
    - change growth margin
    - publish event
    """
    do_some_work()
    event = events.IncumbentRatesCalculated(market=cmd.market)
    outbox.publish(event)
