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
        if self._chips[chip_type] == 0:                 #Deletes the key for that chip type so no residual types of chips with 0 chips are left in the dictionary
            del self._chips[chip_type]

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
    
    def has_chips(self, chip_type: Chip, amount: int) -> bool:
        return self._chips.get(chip_type, 0) >= amount
    
    def clear(self) -> None:
        self._chips.clear()

    def pay_amount(self, amount:int) -> dict:                   #The input will be an amount to pay, and the function will auto select the chips to establish that bet
        if amount > self.total_value():                     #Can the bet be afforded?
            raise ValueError("Not enough balance")
        
        to_remove = {}
        for chip in sorted(self._chips, key= lambda c: c.value, reverse=True):
            if amount <= 0:
                break
            count = self._chips[chip]
            needed = amount // chip.value
            remove_count = min(count, needed)
            if remove_count > 0:
                self._chips[chip] -= remove_count
                to_remove[chip] = remove_count
                amount -= chip.value * remove_count

        if amount > 0:
            raise ValueError("Cannot make exact change")
        
        # Clean up zero-count chips
        self._chips = {chip: cnt for chip, cnt in self._chips.items() if cnt > 0}
        return to_remove