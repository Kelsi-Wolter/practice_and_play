# Design a class to represent a playing card. 
# Now design a class to represent a deck of cards. 
# Using these two classes, implement a favorite card game.

# Kings Corner

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
    
    def __str__(self):
        return f'{str(self.value)} of {self.suite}'
    
    def __repr__(self):
        return f'<Card: {self.value} of {self.suite}>'


class DeckofCards:
    def __init__(self):
        self.cards = [] #(self.create_deck()?) #TODO: change to dictionary so can play cards as 'queen'[4]
    
    def create_deck(self):
        for suite in ['hearts', 'spades', 'diamonds', 'clubs']:
            for num in range(2,11):
                card = Card(num, suite)
                self.cards.append(card)
            for face in ['king', 'queen','jack', 'ace']:
                card = Card(num, suite)
                self.cards.append(card)
    

    def __repr__(self):
        deck = len(self.cards)
        return f'<DeckofCards: {deck} cards currently in deck>'

class HandofCards:
    def __init__(self, num_cards):
        self.num_cards = num_cards
        self.cards = []

    def draw_card(self, num_to_draw, deck):
        
        for num in range(num_to_draw+1):
            card = random.choice(deck.cards).pop() #TODO: make card chose randomly from current deck

    def __repr__(self):
        return f'<Current Hand: {self.cards}'


