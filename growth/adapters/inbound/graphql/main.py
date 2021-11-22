import pathlib

from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL

from growth.adapters.inbound.graphql.mutations.types import mutation
from growth.adapters.inbound.graphql.queries.types import query, tariff

DIR = pathlib.Path(__file__).resolve().parent
type_defs = load_schema_from_path(str(DIR))

schema = make_executable_schema(type_defs, query, tariff, mutation)
app = GraphQL(schema, debug=True)
