from growth.core.application import commands
from growth.core.application.handlers import COMMAND_HANDLERS
from growth.core.domain import types


def test_happy_path(mocker):
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

    command_handler = COMMAND_HANDLERS[command.__class__]
    command_handler(mocker.Mock(), command)

    # TODO - test event is published
