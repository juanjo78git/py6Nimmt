# -*- coding: utf-8 -*-


from pyCard import buildparser


def main():

    # Get Args
    parser = buildparser.build_parser()
    options = parser.parse_args()

    print(options.test)


if __name__ == '__main__':
    main()
