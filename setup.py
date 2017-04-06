#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import py6Nimmt

setup(
    name='py6Nimmt',
    version=py6Nimmt.__version__,
    packages=find_packages(),
    author='juanjo78git',
    author_email='juanjo78@gmail.com',
    description='6 Nimmt! cardgame',
    long_description="README on github: https://github.com/juanjo78git/py6Nimmt",
    install_requires=[],
    url='https://github.com/juanjo78git/py6Nimmt',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment :: Board Games',
    ],
    entry_points={
        'console_scripts': [
            'py6Nimmt = py6Nimmt.py6Nimmt:main',
        ],
    },
)
