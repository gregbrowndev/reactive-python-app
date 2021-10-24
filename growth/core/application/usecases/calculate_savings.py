from growth.core.application import commands, events


def calculate_incumbent_rates(session, cmd: commands.CalculateSavings):
    # retrieve savings, incumbent rates, and Bulb's tariffs
    # calculate savings
    # publish event
    event = events.SavingsCalculated
