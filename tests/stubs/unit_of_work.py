from growth.core.application.ports import IUnitOfWork


class FakeUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.did_commit = False
        self.did_rollback = False

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def commit(self):
        self.did_commit = True

    def rollback(self):
        self.did_rollback = True
