# Design a class to represent a playing card. 
# Now design a class to represent a deck of cards. 
# Using these two classes, implement a favorite card game.

class Card(self):
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
    
    def __repr__(self):
        return f'<Card: Value={self.value}, Suite={self.suite}>'


class DeckofCards(self):
    def __init__(self):
        self.cards = []
    
    def create_deck(self):
        for suite in ['hearts', 'spades', 'diamonds', 'clubs']
            for num in range(2,11):
                card = Card(num, suite)
                DeckofCards.cards.append(card)

