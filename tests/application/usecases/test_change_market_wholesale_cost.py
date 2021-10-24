import decimal
from datetime import datetime

from growth.core.domain import commands, events, types


def test_happy_path(bus):
    """Scenario 1: Market variable rate is changed"""
    # GIVEN
    # some preconditions...

    # WHEN
    command = commands.ChangeMarketWholesaleCost(
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
    resp = bus.issue(command)

    # Then
    assert isinstance(resp, events.MarketWholesaleCostChanged)
    assert resp == events.MarketWholesaleCostChanged(
        market=command.market, price_per_unit=command.price_per_unit
    )
