import time

from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events
from growth.core.domain.functions import do_some_work


def handle(session: Session, outbox: IOutbox, cmd: commands.CalculateSavings):
    """
    Use case: Calculate savings
    Steps:
    - retrieve savings, incumbent rates, and Bulb's tariffs
    - calculate savings
    - publish event
    """
    do_some_work()
    event = events.SavingsCalculated(market=cmd.market)
    outbox.publish(event)
