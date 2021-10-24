import decimal
import uuid
from datetime import datetime

from growth.core.application.ports import IMessageBus
from growth.core.domain import commands, events, types


def test_happy_path(bus: IMessageBus):
    """Scenario 1: Tariff market variable rate is changed"""
    # GIVEN
    # some preconditions...

    # WHEN
    command = commands.ChangeTariffMarketVariableRate(
        tariff_id=types.TariffId(uuid.uuid4()),
        market=types.Market(
            territory=types.Territory.FR,
            region_code=None,
            utility=types.Utility.ELECTRICITY,
            market_type=types.MarketType.RESIDENTIAL,
        ),
        price_per_unit=types.Rate(
            price_per_unit=decimal.Decimal("0.01"), effective_date=datetime(2020, 1, 1)
        ),
    )
    resp = bus.invoke(command)

    # Then
    assert resp == [
        events.TariffMarketVariableRateChanged(
            tariff_id=command.tariff_id,
            market=command.market,
            price_per_unit=command.price_per_unit,
        )
    ]
