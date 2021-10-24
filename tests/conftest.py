import pytest

from growth.bootstrap import bootstrap
from growth.core.application.ports import IMessageBus
from tests.stubs.unit_of_work import FakeUnitOfWork


@pytest.fixture
def bus() -> IMessageBus:
    uow = FakeUnitOfWork()
    return bootstrap(uow=uow)
