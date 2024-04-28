from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import *

@dataclass
class Model:
    storage_location: str
    model_type: str
    training_date: date

    def __hash__(self):
        return hash(self.storage_location)