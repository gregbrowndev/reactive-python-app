from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # Add core settings here
    DATABASE_URL: PostgresDsn = PostgresDsn("postgresql://growth:growth@db:5432/growth")
