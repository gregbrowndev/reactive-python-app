from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from growth.core.application.ports import IUnitOfWork
from growth.settings import Settings


class UnitOfWork(IUnitOfWork):
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
