import pathlib

from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL

from growth.adapters.inbound.graphql.mutations import mutation
from growth.adapters.inbound.graphql.queries import query, tariff

DIR = pathlib.Path(__file__).resolve().parent
SCHEMA_LOCATION = str(DIR.joinpath("schema.graphql"))

type_defs = load_schema_from_path(SCHEMA_LOCATION)
schema = make_executable_schema(type_defs, query, tariff, mutation)
app = GraphQL(schema, debug=True)
