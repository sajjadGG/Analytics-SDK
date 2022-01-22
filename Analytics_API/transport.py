from io import BytesIO
from Event import Event
import requests


class Envelope:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def serialize(self) -> BytesIO:
        pass


class Transport:
    def __init__(self, **kwargs) -> None:
        pass

    def config(self, config) -> None:
        pass

    def send_envelope(self, envelope: Envelope):
        pass


class HTTPTransport(Transport):
    def config(self, config) -> None:
        self.host = config["host"]
        self.endpoint = config["endpoint"]
        self.token = config["token"]

    def __init__(self, **kwargs) -> None:
        if kwargs["config"] is None:
            self.config(
                {
                    "host": kwargs["host"],
                    "endpoint": kwargs["endpoint"],
                    "token": kwargs["token"],
                }
            )
        else:
            pass
        super().__init__()

    def send_envelope(self, envelope: Envelope):
        requests.post(
            self.config["host"] + self.config["endpoint"],
            data=envelope.serialize(),
            headers={"Authorization-Token": self.config["token"]},
        )
