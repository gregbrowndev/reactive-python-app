import decimal
from typing import List, Optional

from ariadne import ObjectType, convert_kwargs_to_snake_case

from growth.adapters.inbound.graphql import model

query = ObjectType("Query")


@query.field("tariffs")
@convert_kwargs_to_snake_case
async def resolve_tariffs(*_) -> List[model.Tariff]:
    return list(model.tariffs.values())


@query.field("tariff")
@convert_kwargs_to_snake_case
async def resolve_tariff(*_, tariff_id: int) -> Optional[model.Tariff]:
    return model.tariffs.get(tariff_id, None)


tariff = ObjectType("Tariff")


@tariff.field("tariffId")
@convert_kwargs_to_snake_case
async def resolve_tariff_id(obj: model.Tariff, *_) -> int:
    print("Called!")
    print(obj)
    return obj.tariff_id


@tariff.field("standardVariableRate")
@convert_kwargs_to_snake_case
async def resolve_standard_variable_rate(obj: model.Tariff, *_) -> decimal.Decimal:
    return obj.standard_variable_rate
