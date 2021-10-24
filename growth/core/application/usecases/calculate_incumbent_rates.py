import time

from growth.core.application import commands, events


def handle(session, cmd: commands.CalculateIncumbentRates):
    """
    Use case: Calculate Incumbent Rates
    Steps:
    - retrieve incumbents
    - change growth margin
    - publish event
    """
    time.sleep(2)
    event = events.IncumbentRatesCalculated(market=cmd.market)
