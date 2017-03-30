#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import pyCard

setup(
    name='pyCard',
    version=pyCard.__version__,
    packages=find_packages(),
    author='juanjo78git',
    author_email='juanjo78@gmail.com',
    description='Cardgame s core',
    long_description="README on github : https://github.com/juanjo78git/pyCard",
    install_requires=[
    ],
    url='https://github.com/juanjo78git/pyCard',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games',
    ],
    entry_points={
        'console_scripts': [
            'pyCard = pyCard.pyCard:main',
        ],
    },
)