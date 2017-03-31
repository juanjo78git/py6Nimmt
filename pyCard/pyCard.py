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
    print(d)
    d.shuffle()
    print('Score: {}'.format(d.score()))
    c = d.draw()
    print(c)
    # print(d)


def iniDeck(d):
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
        d.add(c)
    return d.count()


if __name__ == '__main__':
    main()
