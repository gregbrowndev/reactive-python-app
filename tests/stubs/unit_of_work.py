from unittest import mock

from sqlalchemy.orm import Session

from growth.core.application.ports import IUnitOfWork


class FakeUnitOfWork(IUnitOfWork):
    def __init__(self):
        # TODO - remove session once core dependency is removed
        self.session = mock.create_autospec(Session, instance=True)
        self._did_commit = False
        self._did_rollback = False
        self._is_active = False

    def __enter__(self):
        self._is_active = True

    def __exit__(self, *args):
        self.rollback()

    def is_active(self) -> bool:
        return self._is_active

    def commit(self):
        self._did_commit = True
        self._is_active = False

    def rollback(self):
        self._did_rollback = True
        self._is_active = False
