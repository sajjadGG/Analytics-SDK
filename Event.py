from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    content: str
    gen_time: datetime.datetime
    level: str
