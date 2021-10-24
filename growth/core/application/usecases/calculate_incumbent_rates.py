from growth.core.application import commands, events


def calculate_incumbent_rates(session, cmd: commands.CalculateIncumbentRates):
    # retrieve incumbents
    # change growth margin
    # publish event
    event = events.IncumbentRatesCalculated
