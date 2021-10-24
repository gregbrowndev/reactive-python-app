import decimal
import uuid
from datetime import datetime

from growth.core.application.ports import IMessageBus
from growth.core.domain import commands, events, types


def test_happy_path(bus_reactive: IMessageBus):
    """Scenario 1: Market wholesale cost is changed"""
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
    resp = bus_reactive.invoke(command)

    # Then
    assert resp == [
        events.MarketWholesaleCostChanged(
            market=command.market, price_per_unit=command.price_per_unit
        ),
        events.MarketVariableRateChanged(
            market=command.market,
            price_per_unit=command.price_per_unit,  # doesn't make sense
        ),
        events.TariffMarketVariableRateChanged(
            tariff_id=uuid.UUID("2b1bd95b-3412-4349-8402-70a902dd8d21"),
            market=command.market,
            price_per_unit=command.price_per_unit,  # doesn't make sense
        ),
        events.IncumbentRatesCalculated(market=command.market),
        events.SavingsCalculated(market=command.market),
    ]
