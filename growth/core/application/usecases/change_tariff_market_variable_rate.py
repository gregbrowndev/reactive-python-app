from sqlalchemy.orm import Session

from growth.core.application.ports import IOutbox
from growth.core.domain import commands, events
from growth.core.domain.functions import do_some_work


def handle(
    session: Session, outbox: IOutbox, cmd: commands.ChangeTariffMarketVariableRate
):
    """
    Use case: Change tariff market variable rate
    Steps:
    - retrieve tariff
    - set current market varible rate
    - publish event
    """
    do_some_work()
    event = events.TariffMarketVariableRateChanged(
        tariff_id=cmd.tariff_id, market=cmd.market, price_per_unit=cmd.price_per_unit
    )
    outbox.publish(event)
