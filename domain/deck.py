import random
from card import Suit, Card

class Deck:
    def __init__(self):                 #Auto initiated function to start the deck
        self.cards = self._create_deck()

    def _create_deck():                 #Create new deck (auto initiated)
        cards = []
        for suit in Suit:
            for value in range(2, 15):
                cards.append(Card(value, suit))
        return cards
    
    def shuffle(self):                  #Shuffle all cards in the deck
        random.shuffle(self.cards)

    def deal(self):                 #Deal one card from the top of the deck
        if not self.cards:
            raise "Deck is empty"
        return self.cards.pop()