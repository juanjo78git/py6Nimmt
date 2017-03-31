# -*- coding: utf-8 -*-


class Player(object):
    """ Player """

    def __init__(self, id, name='Player', hand=None):
        self.id = id
        self.name = name
        if hand is None:
            self.hand = []
        else:
            self.hand = hand

    def __str__(self):
        return '{} {:02}'.format(self.name, self.id)

    def __repr__(self):
        return '{} {}'.format(self.id, self.name)
