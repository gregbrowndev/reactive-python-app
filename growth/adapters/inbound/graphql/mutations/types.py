from decimal import Decimal
from typing import Any

from ariadne import ObjectType, convert_kwargs_to_snake_case
from graphql import GraphQLResolveInfo

from growth.adapters.inbound.graphql import model

mutation = ObjectType("Mutation")


@mutation.field("adjustStandardVariableRate")
@convert_kwargs_to_snake_case
async def resolve_adjust_standard_variable_rate(
    obj: Any, info: GraphQLResolveInfo, tariff_id: int, standard_variable_rate: Decimal
):
    try:
        tariff = model.tariffs.get(tariff_id)
        if not tariff:
            return {"status": False, "errors": ["Tariff not found"]}

        tariff.standard_variable_rate = standard_variable_rate
        return {"status": True}

    except Exception as error:
        return {"status": False, "errors": [str(error)]}
