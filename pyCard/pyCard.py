# -*- coding: utf-8 -*-


from pyCard import buildparser
from pyCard import Table


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    print('Players: ' + options.players)
    p = int(options.players)
    t = Table.Table(p)
    c = 0
    e = ''
    while e != 'q' and not t.endgame():
        if c < p:
            c = c + 1
        else:
            c = 1
        e = input("Next Player (q to Quit):")
        if e != 'q':
            t.printBoard()
            t.printPlayer(c)
            t.turnPlayer(c)
            t.printBoard()
            t.printPlayer(c)
        print(''.rjust(60, '='))
    t.stats()


if __name__ == '__main__':
    main()
