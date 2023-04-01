import random


def main():
    c = Card()
    c.selectRandom()
    print(c)


class Card:
    def __init__(self, rank='', suit=''):
        self._rank = rank
        self._suit = suit

    def selectRandom(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'jack', 'queen', 'king', 'ace']
        self._rank = random.choice(ranks)
        self._suit = random.choice(['spades', 'hearts', 'clubs', 'diamonds'])

    def __str__(self):
        return self._rank+' of '+self._suit


main()
