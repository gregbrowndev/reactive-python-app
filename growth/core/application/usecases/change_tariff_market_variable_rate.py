import time

from growth.core.application import commands, events


def handle(session, cmd: commands.ChangeTariffMarketVariableRate):
    """
    Use case: Change tariff market variable rate
    Steps:
    - retrieve tariff
    - set current market varible rate
    - publish event
    """
    time.sleep(2)
    event = events.TariffMarketVariableRateChanged(
        tariff_id=cmd.tariff_id, market=cmd.market, price_per_unit=cmd.price_per_unit
    )
