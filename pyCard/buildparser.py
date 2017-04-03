# -*- coding: utf-8 -*-

import argparse

from pyCard import __version__


def build_parser():
    """ Parser args """
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--players', type=str,
                        dest='players', default='2', metavar='players',
                        help='Number of Players')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser
