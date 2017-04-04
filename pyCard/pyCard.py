# -*- coding: utf-8 -*-


from pyCard import buildparser
from pyCard import Table


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    print('Players: ' + options.players)
    ps = int(options.players)
    t = Table.Table(ps)
    p = 0
    e = ''
    while e != 'Q' and e != 'q' and not t.endgame():
        if p < ps:
            p = p + 1
        else:
            p = 1
        e = input("Next Player (q to Quit):")
        if e != 'q' and e != 'Q':
            t.printBoard()
            t.printPlayer(p)
            c = input_int("Choose a card to play (q to Quit):",
                          1, t.player(p).countHand())
            if c:
                card = t.playCard(p, c)
                b = -1
                if card:
                    print("The played card is lower than all "
                          "the latest cards present on the rows.")
                    b = input_int("Choose a row (q to Quit):",
                                  1, t.countBoards())
                    if b:
                        t.catchBoard(p, b, card)
                    else:
                        e = 'q'
                if e or e != 'q':
                    t.drawCard(p)
            else:
                e = 'q'
        else:
            t.printBoard()
            t.printPlayer(p)
        print(''.rjust(60, '='))
    t.stats()


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


if __name__ == '__main__':
    main()
