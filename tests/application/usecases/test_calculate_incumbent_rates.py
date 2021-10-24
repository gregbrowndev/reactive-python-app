from growth.core.application.ports import IMessageBus
from growth.core.domain import commands, events, types


def test_happy_path(bus: IMessageBus):
    """Scenario 1: Incumbent rates are calculated"""
    # GIVEN
    # some preconditions...

    # WHEN
    command = commands.CalculateIncumbentRates(
        market=types.Market(
            territory=types.Territory.FR,
            region_code=None,
            utility=types.Utility.ELECTRICITY,
            market_type=types.MarketType.RESIDENTIAL,
        )
    )
    resp = bus.invoke(command)

    # Then
    assert resp == [events.IncumbentRatesCalculated(market=command.market)]
