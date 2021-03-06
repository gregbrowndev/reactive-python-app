import typing

from pydantic import BaseSettings

if typing.TYPE_CHECKING:
    # mypy doesn't like default literal string
    # see https://github.com/samuelcolvin/pydantic/issues/1490#issuecomment-630131270
    PostgresDsn = str
else:
    from pydantic import PostgresDsn


"""
Separate core settings from entry point settings, e.g. in toml env file
[core]
database_url = "..."

[flask]
secret_key = "..."
session_cookies_secure = True

[pubsub]
whatever = "..."
"""


class Settings(BaseSettings):
    # Add core settings here
    DATABASE_URL: PostgresDsn = "postgresql://growth:growth@db:5432/growth"
