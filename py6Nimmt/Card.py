# -*- coding: utf-8 -*-


class Card(object):
    """ Card """

    def __init__(self, id, value, suit, score):
        self.id = id
        self.value = value
        self.suit = suit
        self.score = score

    def __cmp__(self, otro):
        diferencia = self.value - otro.value
        if diferencia < 0:
            return -1
        elif diferencia > 0:
            return 1
        else:
            return 0

    def __eq__(self, otro):
        return self.__cmp__(otro) == 0

    def __ne__(self, otro):
        return self.__cmp__(otro) != 0

    def __gt__(self, otro):
        return self.__cmp__(otro) == 1

    def __ge__(self, otro):
        return self.__cmp__(otro) >= 0

    def __le__(self, otro):
        return self.__cmp__(otro) <= 0

    def __lt__(self, otro):
        return self.__cmp__(otro) == -1

    def __str__(self):
        return '{:03}({:02})'.format(self.value, abs(self.score))

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.value, self.suit, self.score)
