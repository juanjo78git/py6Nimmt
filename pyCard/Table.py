# -*- coding: utf-8 -*-

from pyCard import Card
from pyCard import Deck
from pyCard import Player


class Table(object):
    """ Table """

    def __init__(self, numPlayers=2):

        self.deck = Deck.Deck()
        self.iniDeck()
        self.shuffleDeck()

        self.discards = Deck.Deck()

        self.board = [Deck.Deck(), Deck.Deck(), Deck.Deck(), Deck.Deck()]
        for i in range(0, len(self.board)):
            self.board[i].add(self.deck.draw())

        self.players = []
        for i in range(0, numPlayers):
            hand = Deck.Deck()
            for c in range(0, 10):
                hand.add(self.deck.draw())
            self.players.append(Player.Player(i+1, 'Player', hand))

        self.MAX_CARDS_BY_ROW = 6

    def printPlayer(self, id=None):
        for p in self.players:
            if id is None or p.id == id:
                print(str(p) + ':')
                print(p.hand.printCard())
                print('Pile: ' + str(p.pile))

    def printBoard(self):
        i = 1
        print(''.rjust(60, '-'))
        for b in self.board:
            print('{}: {}'.format(i, b))
            i = i + 1
        print(''.rjust(60, '-'))

    def shuffleDeck(self):
        self.deck.shuffle()

    def player(self, id):
        for p in self.players:
            if p.id == id:
                return p

    def boardCorrect(self, card):
        i = 0
        z = -1
        aux = Card.Card(0, 0, 'none', 0)
        for b in self.board:
            if aux <= b.list[-1] and card >= b.list[-1]:
                z = i
            i = i + 1
            aux = b.list[-1]
        if z == -1:
            return None
        else:
            return self.board[z]

    def catchBoard(self, p, b, card):
        b = b - 1
        self.player(p).pile = self.player(p).pile + self.board[b]
        self.board[b].clean()
        self.board[b].add(card)

    def turnPlayer(self, p):
        c = int(input("Choose a card to play:"))
        card = self.player(p).playCard(c)
        if self.boardCorrect(card) is None:
            print("The played card is lower than all "
                  "the latest cards present on the rows.")
            b = int(input("Choose a row:"))
            self.catchBoard(p, b, card)
        else:
            bc = self.boardCorrect(card)
            if bc.count() >= 5:
                self.player(p).pile = self.player(p).pile + bc
                bc.clean()
            bc.add(card)

    def iniDeck(self):
        # Initialize Deck
        # Cartas del 1 al 104
        # Los multiplos de 5 dan 2 puntos
        # Los multiplos de 10, 3 puntos
        # Los multiplos de 11, 5 puntos
        # El 55 da 7 puntos (es múltiplo de 11 y de 5)
        # El resto dan 1 punto
        for i in range(1, 105):
            score = 0
            if i % 10 == 0:
                score = -3
            elif i % 5 == 0:
                score = -2
            if i % 11 == 0:
                score = score - 5
            if score == 0:
                score = -1
            c = Card.Card(i, i, 'none', score)
            self.deck.add(c)
        return self.deck.count()

    def __str__(self):
        return 'Deck:{} Discards:{} Players:{}'.format(self.deck.count(),
                                                       self.discards.count(),
                                                       len(self.players))

    def __repr__(self):
        return 'Deck:{} Discards:{} Players:{}'.format(self.deck.count(),
                                                       self.discards.count(),
                                                       len(self.players))
