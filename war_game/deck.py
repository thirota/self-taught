
from random import shuffle

from card import Card

class Deck:

    def __init__(self):

        # TODO cards should be _cards as a private member?
        self.cards = []

        # values 2..14
        # 2 is "one", 14 is "Ace"
        for i in range(2, 15):

            # suits 0..3
            for j in range(4):
                self.cards.append(Card(i, j))

        shuffle(self.cards)


    def rm_card(self):

        # None when cards is empty
        if len(self.cards) == 0:
            return

        return self.cards.pop()



# DEBUG
deck = Deck()
print(len(deck.cards))
for card in deck.cards:
    print(card)

card = deck.rm_card()        
print(card)
print(len(deck.cards))

card = deck.rm_card()
print(card)
print(len(deck.cards))

