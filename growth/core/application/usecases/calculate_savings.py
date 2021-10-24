import time

from growth.core.application import commands, events


def handle(session, cmd: commands.CalculateSavings):
    """
    Use case: Calculate savings
    Steps:
    - retrieve savings, incumbent rates, and Bulb's tariffs
    - calculate savings
    - publish event
    """
    time.sleep(2)
    event = events.SavingsCalculated(market=cmd.market)
