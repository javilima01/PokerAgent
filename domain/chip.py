from enum import Enum

class Chip(Enum):                   #Based on the international code. Could change depending on poker service
    WHITE = "1"
    RED = "5"
    BLUE = "10"
    GREY = "20"
    GREEN = "25"
    ORANGE = "50"
    BLACK = "100"
    PINK = "250"
    PURPLE = "500"
    YELLOW = "1000"
    LIGHT_BLUE = "2000"
    BROWN = "5000"

class ChipStack:
    def __init__(self):
        self._chips: dict[Chip, int] = ()                   #Creation of empty dictionary, indicating the type of the key and values [Type of chip, amount of chips of that type]
    
    def add_chips(self, chip_type: Chip, amount: int) -> None:
        current = self._chips.get(chip_type, 0)
        if amount <= 0:
            raise ValueError("Cannot add zero or negative chips")
        self._chips[chip_type] = current + amount

    def remove_chips(self, chip_type: Chip, amount: int) -> None:
        current = self._chips.get(chip_type, 0)
        if amount <= 0 or amount > current:
            raise ValueError("Cannot remove zero or negative chips")
        self._chips[chip_type] = current - amount
        if self._chips[chip_type] == 0:
            del self._chips[chip_type]                  #Deletes the key for that chip type so no residual types of chips with 0 chips are left in the dictionary

    def get_stack_status(self) -> dict[str, int]:
        status = {}
        for chip, amount in self._chips.items():
            status[chip.name] = amount
        return status

    def total_value(self) -> int:
        total = 0
        for chip, amount in self._chips.items():
            total += chip.value * amount
        return total