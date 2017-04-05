# -*- coding: utf-8 -*-

import argparse

from argparse import RawTextHelpFormatter
from py6Nimmt import __version__


def build_parser():
    """ Parser args """
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description='6 Nimmt! cardgame')

    parser.add_argument('-p', '--players', type=str,
                        dest='players', default='2', metavar='players',
                        help='Number of Players')

    parser.add_argument('-r', '--rules',
                        dest='rules', action='store_true',
                        help='Show rules')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser
