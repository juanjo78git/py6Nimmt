# -*- coding: utf-8 -*-

from py6Nimmt import Card
from py6Nimmt import Deck
from py6Nimmt import Player


class Table(object):
    """ Table """

    def __init__(self, numPlayers=2):

        self.deck = Deck.Deck()
        self.iniDeck()
        self.shuffleDeck()

        self.discards = Deck.Deck()

        self.board = [Deck.Deck(0), Deck.Deck(1), Deck.Deck(2), Deck.Deck(3)]
        for i in range(0, len(self.board)):
            self.board[i].add(self.deck.draw())

        self.players = []
        for i in range(0, numPlayers):
            hand = Deck.Deck(i+1)
            for c in range(0, 10):
                hand.add(self.deck.draw())
            self.players.append(Player.Player(i+1, 'Player', hand))

    def countBoards(self):
        return len(self.board)

    def countDeck(self):
        return len(self.deck)

    def countDiscard(self):
        return len(self.discards)

    def printPlayer(self, id=None):
        s = ''
        for p in self.players:
            if id is None or p.id == id:
                s = s + str(p) + ':' + '\n'
                s = s + p.hand.printCard() + '\n'
                s = s + 'Pile: ' + str(p.pile) + '\n'
        return s

    def printBoard(self):
        i = 1
        s = ''.rjust(52, '-') + 'Deck: ' + str(self.deck.count()) + '\n'
        for b in self.board:
            s = s + '{}: {} |'.format(i, b)
            for z in range(0, 5 - b.count()):
                s = s + '         |'
            s = s + '\n'
            i = i + 1
        s = s + ''.rjust(60, '-')
        return s

    def shuffleDeck(self):
        self.deck.shuffle()

    def player(self, id):
        for p in self.players:
            if p.id == id:
                return p

    def boardCorrect(self, card):
        i = 0
        z = -1
        anterior = Card.Card(0, 0, 'none', 0)
        for b in self.board:
            if card >= b.lastCard() and anterior <= b.lastCard():
                z = i
                anterior = b.lastCard()
            i = i + 1
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
        # DEPRECATED
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
        if self.deck.count() > 0:
            self.player(p).addHand(self.deck.draw())

    def playCard(self, p, c):
        card = self.player(p).playCard(c)
        if self.boardCorrect(card):
            bc = self.boardCorrect(card)
            if bc.count() >= 5:
                self.player(p).pile = self.player(p).pile + bc
                bc.clean()
            bc.add(card)
            return None
        else:
            return card

    def drawCard(self, p):
        if self.deck.count() > 0:
            self.player(p).addHand(self.deck.draw())

    def endgame(self):
        fin = True
        if self.deck.count() != 0:
            fin = False
        for p in self.players:
            if p.countHand() != 0:
                fin = False
        return fin

    def stats(self):
        s = ''.rjust(60, '=') + '\n'
        for p in self.players:
            s = s + '{}: {:03}'.format(p, p.score()) + '\n'
            s = s + p.printPile() + '\n'
        s = s + ''.rjust(60, '=')
        return s

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

    def printRules(self):
        text = ('Rules'
                '\n-----\n\n'
                'At each turn, each player selects a '
                'card to play, and put his card at the '
                'end of one of the four rows '
                'on the table, following these rules:'
                '\n\n'
                '- The card must be put on a row where '
                'the latest (end) card is lower in value '
                'than the card that is about to be '
                'played.'
                '\n'
                '- The card must be put on the row where '
                'the latest (end) card is the closest in '
                'value to the card that is about to be '
                'played (if your card is 33, then place '
                'it next to the 30 not the 29, for '
                'example)'
                '\n'
                '- If the row where the played card must '
                'be placed already contains 5 cards (the '
                'player''s card is the 6th), the player '
                'must gather the 5 cards on the table, '
                'leaving only the 6th card in their '
                'place to start a new row. '
                'The gathered cards must be taken '
                'separated and never mixed with the hand '
                'cards. The sum of the number of cattle '
                'head on the gathered cards will be '
                'calculated at the end of the round.'
                '\n'
                '- If the played card is lower than all '
                'the latest cards present on the four '
                'rows, the player must choose a row '
                'and gather the cards on that row '
                '(usually the row with the fewest cattle '
                'heads), leaving only the played card on '
                'the row.'
                '\n'
                '- The cards of all the players are '
                'played following these rules, from the '
                'lowest player card to the highest one.'
                '\n'
                'At the end of the turn, the players '
                'each select a new card to play; this is '
                'repeated for 10 turns until all the '
                'cards in the hand are played.'
                '\n'
                'After the 10 turns, each player counts '
                'the cattle heads on the cards gathered '
                'from the table during the round.'
                '\n'
                'The winner is the player who has '
                'collected the fewest cattle heads.'
                '\n\n'
                'Sample card:'
                '\n------------\n\n'
                '004(01)'
                '\n'
                '004 is card value and 01 is the number '
                'of cattle heads (in parentheses).')
        return text
