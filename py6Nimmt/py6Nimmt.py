# -*- coding: utf-8 -*-


from py6Nimmt import buildparser
from py6Nimmt import Table
import os


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    ps = int(options.players)
    t = Table.Table(ps)

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
        clearscr()
        e = input('Next Player (q to Quit):')
        if e != 'q' and e != 'Q':
            print(t.printBoard())
            print(t.printPlayer(p))
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
        else:
            print(t.printBoard())
            print(t.printPlayer(p))
        print(''.rjust(60, '='))
    clearscr()
    print(t.stats())


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
