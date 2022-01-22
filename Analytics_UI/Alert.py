from dataclasses import dataclass
from enum import Enum
from logging import WARNING
from sre_constants import SUCCESS


class AlertVarient(Enum):
    ERROR = 1
    WARNING = 2
    INFO = 3
    SUCCESS = 4


@dataclass
class Alert:
    title: str
    content: str
    alertVarient: AlertVarient


class Subscriber:
    def __init__(self, contact) -> None:
        self.contact = contact

    def consume(self, alert: Alert):
        pass


class EmailSubscriber(Subscriber):
    def consume(self, alert: Alert):
        # TODO:send email
        return super().consume(alert)
