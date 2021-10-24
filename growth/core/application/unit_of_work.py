from typing import Protocol

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from growth.settings import Settings


class IUnitOfWork(Protocol):
    def __enter__(self) -> "IUnitOfWork":
        ...

    def __exit__(self, *args):
        ...

    def commit(self):
        ...

    def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):
    session: Session

    def __init__(self, settings: Settings, session_factory=None):
        if session_factory is None:
            session_factory = sessionmaker(bind=create_engine(settings.DATABASE_URL))
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
