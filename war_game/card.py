
class Card:

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """suit is decimal number"""
        self.value = v
        self.suit = s

    # < operator
    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False

        return False

    # > operator
    def __gt__(self, c2):
        if self.value > c2.value:
            return True

        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False

        return False

    # print()
    def __repr__(self):
       v = self.values[self.value] + " of " + self.suits[self.suit]
       return v 


# DEBUG
spade_one = Card(14, 0)
print(spade_one)
heart_four = Card(4, 1)
print(heart_four)
diamond_king = Card(13, 2)
print(diamond_king)
club_eight = Card(8, 3)
print(club_eight)
