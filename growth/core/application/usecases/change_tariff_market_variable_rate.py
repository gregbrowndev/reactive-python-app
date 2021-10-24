from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeTariffMarketVariableRate):
    # retrieve tariff
    # set current market varible rate
    # publish event
    event = events.TariffMarketVariableRateChanged
