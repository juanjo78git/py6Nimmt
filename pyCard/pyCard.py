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
    while e != 'q' and not t.endgame():
        if p < ps:
            p = p + 1
        else:
            p = 1
        e = input("Next Player (q to Quit):")
        if e != 'q':
            t.printBoard()
            t.printPlayer(p)
            c = int(input("Choose a card to play:"))
            card = t.playCard(p, c)
            if card:
                print("The played card is lower than all "
                      "the latest cards present on the rows.")
                b = int(input("Choose a row:"))
                t.catchBoard(p, b, card)
            t.drawCard(p)
        else:
            t.printBoard()
            t.printPlayer(p)
        print(''.rjust(60, '='))
    t.stats()


if __name__ == '__main__':
    main()
