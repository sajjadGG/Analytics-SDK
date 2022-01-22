from dataclasses import dataclass
from Alert import EmailSubscriber
from front import Dashboard


class Account:
    def __init__(
        self,
        username,
        email,
    ) -> None:
        self.username = username
        self.email = email
        self.subscriber = EmailSubscriber(self.email)


class Workspace:
    def __init__(self, name: str, workspaceID: str) -> None:
        self.name = name
        self.workspaceID = workspaceID
        self.accounts = []
        self.dashboards = []

    def register(self, acc: Account):
        pass

    def getAccounts(self):
        return self.accounts

    def addDashboard(dashboard: Dashboard):
        pass

    def getDashboards(self):
        return self.dashboards
