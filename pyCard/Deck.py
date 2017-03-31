# -*- coding: utf-8 -*-

from random import shuffle


class Deck(object):
    """ Deck """

    def __init__(self, list=None):
        if list is None:
            self.list = []
        else:
            self.list = list

    def count(self):
        return len(self.list)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def add(self, card):
        self.list.append(card)

    def draw(self):
        try:
            return self.list.pop()
        except IndexError as e:
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

    def __str__(self):
        return ' '.join('{} |'.format(c) for c in self.list).rstrip(' |')

    def __repr__(self):
        return 'Deck with {} cards'.format(self.count())
