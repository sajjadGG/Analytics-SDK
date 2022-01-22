from distutils.command.config import config
from io import BytesIO
from Event import Event
import requests
from utils import parse_config


class Envelope:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def serialize(self):
        pass


class HTTPEnvelope(Envelope):
    def serialize(self) -> BytesIO:
        return {"events": self.event}

    def length(self):
        return len(self.events)


class Transport:
    def __init__(self, config) -> None:
        self.configurate(config)

    def configurate(self, config) -> None:
        pass

    def send_envelope(self, envelope: Envelope):
        pass

    def capture(self, event: Event):
        pass


class HTTPTransport(Transport):
    def configurate(self, config) -> None:
        self.host = config["host"]
        self.endpoint = config["endpoint"]
        self.token = config["token"]
        self.buffer_size = int(config["buffer"])
        self.current_envelope = HTTPEnvelope()

    def send_envelope(self, envelope: Envelope):
        requests.post(
            self.config["host"] + self.config["endpoint"],
            data=envelope.serialize(),
            headers={"Authorization-Token": self.config["token"]},
        )

    def capture(self, event: Event):
        # TODO:incoparte more sophisiticated sending mechanism
        self.current_envelope.add_event(event)
        if self.current_envelope.length() > self.buffer_size:
            # TODO: async
            self.send_envelope(self.current_envelope)


def create_transport(config_path):
    config = parse_config(config_path)
    # TODO: based on config decide what transport to return
    if "HTTP" in config["Transport"]:
        return HTTPTransport(config)
    else:
        raise NotImplementedError()
