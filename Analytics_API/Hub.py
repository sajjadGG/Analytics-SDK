from multiprocessing.connection import Client
from Event import Event
from Client import Client, SimpleClinet
from transport import create_transport


class Broker:
    class __Broker:
        def __init__(self, config_path="config.yaml") -> None:
            # TODO: use Factory method or other design pattern to create Broker based on Config
            self.transport = create_transport(config_path)

        def capture(self, event: Event) -> None:
            self.transport.capture(event)

    instance = None

    def __init__(self, config):
        if not Broker.instance:
            Broker.instance = Broker.__Broker(config)
        return Broker.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


def init(token) -> None:
    """
    intialization step and create a Hub
    should be called once
    (if called many times should not cause any problem)

    Args:
        token ([type]): [description]
    """
    b = Broker()  # pass config
