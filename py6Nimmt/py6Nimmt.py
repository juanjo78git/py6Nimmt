# -*- coding: utf-8 -*-


from py6Nimmt import buildparser
from py6Nimmt import Table
import os
import sys
import gettext
_ = gettext.gettext


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()
    # gettext
    if options.lang != '':
        os.environ['LANG'] = options.lang
    else:
        if sys.platform.startswith('win'):
            import locale
            if os.getenv('LANG') is None:
                lang = locale.getdefaultlocale()
                os.environ['LANG'] = lang
    gettext.textdomain('py6Nimmt')
    gettext.bindtextdomain('py6Nimmt', './py6Nimmt/locale')

    # print('Locale: ' + os.environ['LANG'])

    if options.rules:
        print(printRules())
        exit()

    ps = int(options.players)
    if ps < 1 or ps > 10:
        print(_('The argument value of -ps must be a number between 1 and 10:')
              + ' {}.'.format(ps))
        exit()
    pn = list(options.namesPlayers)
    if ps < len(pn):
        ps = len(pn)

    t = Table.Table(ps, pn)

    p = 0
    e = ''

    while e != 'Q' and e != 'q' and not t.endgame():
        if p < ps:
            p = p + 1
        else:
            p = 1
        e = input(_('Next Player (q to Quit):'))
        clearscr()
        if e != 'q' and e != 'Q':
            print(t.printBoard())
            print(t.printPlayer(p))
            print(_('Pile: ') + t.printPlayerPile(p))
            c = input_int(_('Choose a card to play (q to Quit):'),
                          1, t.player(p).countHand())
            if c:
                card = t.playCard(p, c)
                b = -1
                if card:
                    print(_('The played card is lower than all '
                          'the latest cards present on the rows.'))
                    b = input_int(_('Choose a row to catch (q to Quit):'),
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
            print(_('Pile: ') + t.printPlayerPile(p))
        else:
            print(t.printBoard())
            print(t.printPlayer(p))
            print(_('Pile: ') + t.printPlayerPile(p))
        print(''.rjust(60, '='))
    clearscr()
    print(t.stats())
    print(_('Winner: ') + str(t.winner()))


def input_int(text='Insert a number (q to Quit):', minim=0, maxim=10):
    while True:
        valor = input(text)
        try:
            if valor == 'q' or valor == 'Q':
                return None
            else:
                valor = int(valor)
                if valor >= minim and valor <= maxim:
                    return valor
        except ValueError:
            print(_('Value error'))


def clearscr():
    osname = os.name
    if osname == 'posix':
        os.system('clear')
    elif osname == 'nt' or osname == 'dos':
        os.system('cls')
    else:
        print('\n' * 30)


def printRules():
    txt = _('text_rules')
    return txt


if __name__ == '__main__':
    main()
