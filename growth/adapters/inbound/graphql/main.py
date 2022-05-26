import pathlib

from ariadne import load_schema_from_path, make_executable_schema, upload_scalar, snake_case_fallback_resolvers
from ariadne.asgi import GraphQL

from growth.adapters.inbound.graphql.mutations.types import mutation
from growth.adapters.inbound.graphql.queries.types import query, tariff

DIR = pathlib.Path(__file__).resolve().parent
type_defs = load_schema_from_path(str(DIR))

schema = make_executable_schema(type_defs, query, tariff, mutation, upload_scalar, snake_case_fallback_resolvers)
app = GraphQL(schema, debug=True)
