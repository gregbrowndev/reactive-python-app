import decimal
from datetime import datetime

from growth.core.application.ports import IMessageBus
from growth.core.domain import commands, events, types


def test_happy_path(bus: IMessageBus):
    """Scenario 1: Growth margin is changed"""
    # GIVEN
    # some preconditions...

    # WHEN
    command = commands.ChangeMarketGrowthMargin(
        market=types.Market(
            territory=types.Territory.FR,
            region_code=None,
            utility=types.Utility.ELECTRICITY,
            market_type=types.MarketType.RESIDENTIAL,
        ),
        margin=types.Rate(
            price_per_unit=decimal.Decimal("0.01"), effective_date=datetime(2020, 1, 1)
        ),
    )
    resp = bus.invoke(command)

    # Then
    assert resp == [
        events.MarketGrowthMarginChanged(market=command.market, margin=command.margin)
    ]
