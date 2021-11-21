from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Tariff:
    tariff_id: int
    standard_variable_rate: Decimal


tariffs = {1: Tariff(tariff_id=1, standard_variable_rate=Decimal("0.0123"))}
