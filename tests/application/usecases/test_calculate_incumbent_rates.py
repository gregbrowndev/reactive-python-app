from growth.core.domain import commands, events, types


def test_happy_path(bus):
    """Scenario 1: Incumbent rates are calculated"""
    # WHEN
    command = commands.CalculateIncumbentRates(
        market=types.Market(
            territory=types.Territory.FR,
            region_code=None,
            utility=types.Utility.ELECTRICITY,
            market_type=types.MarketType.RESIDENTIAL,
        )
    )
    resp = bus.issue(command)

    # Then
    assert isinstance(resp, events.IncumbentRatesCalculated)
    assert resp == events.IncumbentRatesCalculated(market=command.market)
