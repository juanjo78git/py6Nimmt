# -*- coding: utf-8 -*-

from py6Nimmt import Deck


class Player(object):
    """ Player """

    def __init__(self, id, name='Player', hand=None, pile=None):
        self.id = id
        self.name = name
        if hand is None:
            self.hand = Deck.Deck(id)
        else:
            self.hand = hand
        if pile is None:
            self.pile = Deck.Deck(id)
        else:
            self.pile = pile

    def printPile(self):
        return str(self.pile.printCard())

    def printHand(self):
        return str(self.hand.printCard())

    def countHand(self):
        return self.hand.count()

    def countPile(self):
        return self.pile.count()

    def score(self):
        return self.pile.score()

    def addPile(self, card):
        self.pile.add(card)

    def addHand(self, card):
        self.hand.add(card)

    def playCard(self, id):
        return self.hand.deleteCard(id)

    def __str__(self):
        return '{} {:02}'.format(self.name, self.id)

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)

    def __eq__(self, otro):
        if self.id == otro.id:
            return True
        else:
            return False

    def __ne__(self, otro):
        if self.id != otro.id:
            return True
        else:
            return False

    def __cmp__(self, otro):
        diferencia = self.score() - otro.score()
        if diferencia < 0:
            return -1
        elif diferencia > 0:
            return 1
        else:
            return 0

    def __gt__(self, otro):
        return self.__cmp__(otro) == 1

    def __ge__(self, otro):
        return self.__cmp__(otro) >= 0

    def __le__(self, otro):
        return self.__cmp__(otro) <= 0

    def __lt__(self, otro):
        return self.__cmp__(otro) == -1
