import pytest

from growth.bootstrap import bootstrap
from growth.core.application import handlers
from growth.core.application.ports import IMessageBus
from tests.stubs.unit_of_work import FakeUnitOfWork


@pytest.fixture
def bus(bus_reactive) -> IMessageBus:
    """
    Returns a message bus with no reactive event handling
    """
    uow = FakeUnitOfWork()
    event_handlers = {key: [] for key, _ in handlers.EVENT_HANDLERS.items()}
    return bootstrap(uow=uow, event_handlers=event_handlers)


@pytest.fixture
def bus_reactive() -> IMessageBus:
    uow = FakeUnitOfWork()
    return bootstrap(uow=uow)
