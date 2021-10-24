import uuid

from sqlalchemy.orm import Session

from growth.core.application.ports import IInbox
from growth.core.domain import commands, events, types


def handle_market_growth_margin_changed(
    session: Session, inbox: IInbox, event: events.MarketGrowthMarginChanged
):
    command = commands.ChangeMarketVariableRate(
        market=event.market,
        price_per_unit=event.margin,  # doesn't really make sense
    )
    inbox.invoke(command)


def handle_market_wholesale_cost_changed(
    session: Session, inbox: IInbox, event: events.MarketWholesaleCostChanged
):
    command = commands.ChangeMarketVariableRate(
        market=event.market,
        price_per_unit=event.price_per_unit,  # doesn't really make sense
    )
    inbox.invoke(command)


def handle_market_variable_rate_changed(
    session: Session, inbox: IInbox, event: events.MarketVariableRateChanged
):
    # Fetch IDs of tariffs in market. Note, this should be its own command
    tariff_ids = [types.TariffId(uuid.UUID("2b1bd95b-3412-4349-8402-70a902dd8d21"))]

    for tariff_id in tariff_ids:
        command = commands.ChangeTariffMarketVariableRate(
            tariff_id=tariff_id,
            market=event.market,
            price_per_unit=event.price_per_unit,
        )
        inbox.invoke(command)


def handle_tariff_market_variable_rate_changed(
    session: Session, inbox: IInbox, event: events.TariffMarketVariableRateChanged
):
    command = commands.CalculateIncumbentRates(market=event.market)
    inbox.invoke(command)


def handle_incumbent_rates_calculated(
    session: Session, inbox: IInbox, event: events.IncumbentRatesCalculated
):
    command = commands.CalculateSavings(market=event.market)
    inbox.invoke(command)
