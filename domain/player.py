from typing import Dict
from domain.chip import Chip, ChipStack

class Player:
    def __init__(self, name: str, stack: ChipStack):
        self.name = name
        self.stack = stack