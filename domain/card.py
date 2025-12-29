from enum import Enum

class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

#No class is created with the possible values (A, 2, 3, ..., J, Q, K) since the poker program will need later to use the numbers for math and operations.

class Card:
    def __init__(self, value: int, suit: Suit):
        self.value = value
        self.suit = suit