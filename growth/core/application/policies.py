import uuid

from growth.core.application import commands, events
from growth.core.application.ports import IInbox
from growth.core.domain import types


def handle_market_growth_margin_changed(
    session, inbox: IInbox, event: events.MarketGrowthMarginChanged
):
    command = commands.ChangeMarketVariableRate(
        market=event.market,
        region_code=event.region_code,
        price_per_unit=event.margin,  # doesn't really make sense
    )
    # dispatch command


def handle_market_wholesale_cost_changed(
    session, inbox: IInbox, event: events.MarketWholesaleCostChanged
):
    command = commands.ChangeMarketVariableRate(
        market=event.market,
        region_code=event.region_code,
        price_per_unit=event.price_per_unit,  # doesn't really make sense
    )
    # dispatch command


def handle_market_variable_rate_changed(
    session, inbox: IInbox, event: events.MarketVariableRateChanged
):
    # Fetch IDs of tariffs in market. Note, this should be its own command
    tariff_ids = [types.TariffId(uuid.uuid4())]

    for tariff_id in tariff_ids:
        command = commands.ChangeTariffMarketVariableRate(
            tariff_id=tariff_id,
            market=event.market,
            price_per_unit=event.price_per_unit,
        )
        # dispatch command


def handle_tariff_market_variable_rate_changed(
    session, inbox: IInbox, event: events.TariffMarketVariableRateChanged
):
    command = commands.CalculateIncumbentRates(market=event.market)
    # dispatch command


def handle_incumbent_rates_calculated(
    session, inbox: IInbox, event: events.IncumbentRatesCalculated
):
    command = commands.CalculateSavings(market=event.market)
    # dispatch command
