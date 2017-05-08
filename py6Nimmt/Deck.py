# -*- coding: utf-8 -*-

from random import shuffle


class Deck(object):
    """ Deck """

    def __init__(self, id=0, list=None):
        self.id = id
        if list is None:
            self.list = []
        else:
            self.list = list

    def count(self):
        return len(self.list)

    def isEmpty(self):
        return bool(self.list == [])

    def add(self, card):
        if not(card is None):
            self.list.append(card)

    def draw(self):
        try:
            return self.list.pop()
        except IndexError:
            return None

    def shuffle(self):
        shuffle(self.list)

    def clean(self):
        self.list = []

    def score(self):
        i = 0
        for c in self.list:
            i = i + c.score
        return i

    def showCard(self, id):
        # id is card's position (1 is first position)
        id = id - 1
        if id >= 0 and id < self.count() and self.count() > 0:
            return self.list[id]
        else:
            return None

    def lastCard(self):
        if self.count() > 0:
            return self.list[-1]
        else:
            return None

    def deleteCard(self, id):
        # id is card's position (1 is first position)
        id = id - 1
        if id >= 0 and id < self.count() and self.count() > 0:
            # c = self.list[id]
            # del self.list[id]
            # return c
            return self.list.pop(id)
        else:
            return None

    def printCard(self):
        s = ''
        i = 1
        for c in self.list:
            s = '{} {:02}: {} |'.format(s, i, c).rstrip(' |')
            if i % 5 == 0:
                s = s + '\n'
            i = i + 1
        return s

    def __str__(self):
        return ' '.join('{} |'.format(c) for c in self.list).rstrip(' |')

    def __repr__(self):
        return '{:03}'.format(self.count())

    def __add__(self, otro):
        return Deck(self.id, self.list + otro.list)
