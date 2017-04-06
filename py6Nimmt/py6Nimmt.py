# -*- coding: utf-8 -*-


from py6Nimmt import buildparser
from py6Nimmt import Table
import os


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    ps = int(options.players)
    if ps < 1 or ps > 10:
        print('The argument value of -ps ' +
              'must be a number between 1 and 10: {}.'.format(ps))
        exit()
    pn = list(options.namesPlayers)
    if ps < len(pn):
        ps = len(pn)
    t = Table.Table(ps, pn)

    if options.rules:
        print(t.printRules())
        exit()

    p = 0
    e = ''

    while e != 'Q' and e != 'q' and not t.endgame():
        if p < ps:
            p = p + 1
        else:
            p = 1
        e = input('Next Player (q to Quit):')
        clearscr()
        if e != 'q' and e != 'Q':
            print(t.printBoard())
            print(t.printPlayer(p))
            print('Pile: ' + t.printPlayerPile(p))
            c = input_int('Choose a card to play (q to Quit):',
                          1, t.player(p).countHand())
            if c:
                card = t.playCard(p, c)
                b = -1
                if card:
                    print('The played card is lower than all '
                          'the latest cards present on the rows.')
                    b = input_int('Choose a row (q to Quit):',
                                  1, t.countBoards())
                    if b:
                        t.catchBoard(p, b, card)
                    else:
                        e = 'q'
                if e or e != 'q':
                    t.drawCard(p)
            else:
                e = 'q'
            print(t.printBoard())
            print(t.printPlayer(p))
            print('Pile: ' + t.printPlayerPile(p))
        else:
            print(t.printBoard())
            print(t.printPlayer(p))
            print('Pile: ' + t.printPlayerPile(p))
        print(''.rjust(60, '='))
    clearscr()
    print(t.stats())
    print('Winner: ' + str(t.winner()))


def input_int(text='Insert a number (q to Quit):', min=0, max=10):
    while True:
        valor = input(text)
        try:
            if valor == 'q' or valor == 'Q':
                return None
            else:
                valor = int(valor)
                if valor >= min and valor <= max:
                    return valor
        except ValueError:
            print('Value error')


def clearscr():
    osname = os.name
    if osname == 'posix':
        os.system('clear')
    elif osname == 'nt' or osname == 'dos':
        os.system('cls')
    else:
        print('\n' * 30)


if __name__ == '__main__':
    main()
