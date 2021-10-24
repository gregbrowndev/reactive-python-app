from growth.core.application import commands, events


def handle(session, cmd: commands.CalculateIncumbentRates):
    # retrieve incumbents
    # change growth margin
    # publish event
    event = events.IncumbentRatesCalculated
