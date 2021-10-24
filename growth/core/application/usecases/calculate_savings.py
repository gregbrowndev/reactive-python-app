from growth.core.application import commands, events


def handle(session, cmd: commands.CalculateSavings):
    # retrieve savings, incumbent rates, and Bulb's tariffs
    # calculate savings
    # publish event
    event = events.SavingsCalculated
