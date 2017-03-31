# -*- coding: utf-8 -*-


from pyCard import buildparser
from pyCard import Card
from pyCard import Deck


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    print(options.test)

    d = Deck.Deck()
    iniDeck(d)
    d.shuffle()
    print(d)
    print('Score: {}'.format(d.score()))
    c = d.draw()
    print(c)
    print(d)


def iniDeck(d):
    for i in range(1, 11):
        s1 = i % 10
        s2 = i % 5
        if s1 == 0:
            c = Card.Card(i, i, 'none', -10)
        elif s2 == 0:
            c = Card.Card(i, i, 'none', -5)
        else:
            c = Card.Card(i, i, 'none', -1)
        d.add(c)
    return d.count()


if __name__ == '__main__':
    main()
