# -*- coding: utf-8 -*-


class Card(object):
    """ Card """

    def __init__(self, id, value, suit, score):
        self.id = id
        self.value = value
        self.suit = suit
        self.score = score

    def __str__(self):
        # return '{} {} {} {}'.format(
        #                      self.id, self.value, self.suit, self.score)
        return '{:03}({:02})'.format(self.value, abs(self.score))

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.value, self.suit, self.score)
