from Event import Event
from Hub import Broker
from datetime import datetime


class Client:
    """[summary]
    abstract class for all Clients should inheriet this class
    this class is in pub sub design patter as a publisher
    """

    # TODO: add token and configs and necessary initialization steps.
    def __init__(self, name: str, broker: Broker) -> None:
        self._name = name
        self._broker = broker

    # TODO: add topic?
    def pub(self, event: Event):
        self._broker.capture(event)


class SimpleClinet(Client):
    def __init__(self) -> None:
        pass

    def capture_message(self, msg: str) -> None:
        self.pub(Event(msg, datetime.now()))
