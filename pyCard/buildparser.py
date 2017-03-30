# -*- coding: utf-8 -*-

import argparse

from pyCard import __version__


def build_parser():
    """ Parser args """
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--test', type=str,
                        dest='test', default='Test pyCard', metavar='test',
                        help='Print test')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser
