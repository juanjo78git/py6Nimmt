# py6Nimmt

[![travis-ci][badge-travis]][travis]
[![coveralls-io][badge-coveralls]][coveralls]
[![Dependency Status](https://www.versioneye.com/user/projects/58f13f1e0f9f350049e37006/badge.svg?style=flat-square)](https://www.versioneye.com/user/projects/58f13f1e0f9f350049e37006)
[![pypi-version][badge-pypi-version]][pypi]
[![Open issues][badge-issues]][issues]
[![License][badge-license]][license]

## Description

6 Nimmt! cardgame.

## Rules 

At each turn, each player selects a card to play, and put his card at the end of one of the four rows on the table, following these rules:

* The card must be put on a row where the latest (end) card is lower in value than the card that is about to be played.
* The card must be put on the row where the latest (end) card is the closest in value to the card that is about to be played (if your card is 33, then place it next to the 30 not the 29, for example)
* If the row where the played card must be placed already contains 5 cards (the player's card is the 6th), the player must gather the 5 cards on the table, leaving only the 6th card in their place to start a new row. The gathered cards must be taken separated and never mixed with the hand cards. The sum of the number of cattle head on the gathered cards will be calculated at the end of the round.
* If the played card is lower than all the latest cards present on the four rows, the player must choose a row and gather the cards on that row (usually the row with the fewest cattle heads), leaving only the played card on the row.
* The cards of all the players are played following these rules, from the lowest player card to the highest one.

At the end of the turn, the players each select a new card to play; this is repeated for 10 turns until all the cards in the hand are played.

After the 10 turns, each player counts the cattle heads on the cards gathered from the table during the round.

The winner is the player who has collected the fewest cattle heads.

You can read complete rules in https://en.wikipedia.org/wiki/6_Nimmt!#Rules

### Sample card:

  004(01)

  004 is card value and 01 is the number of cattle heads (in parentheses).

## System requirements

* Python3


## Instructions
### Installation

```shell
$ pip install py6Nimmt
```

For developers:
```shell
git clone https://github.com/juanjo78git/py6Nimmt.git
cd py6Nimmt
$ pip install -e . 
$ python -m py6Nimmt.py6Nimmt  # Or run without install
```


## License

MIT



[bad-travis]:https://api.travis-ci.org/juanjo78git/py6Nimmt.svg?branch=master
[badge-travis]:https://img.shields.io/travis/juanjo78git/py6Nimmt.svg?style=flat-square
[badge-coveralls]:https://img.shields.io/coveralls/juanjo78git/py6Nimmt.svg?style=flat-square
[badge-issues]:http://img.shields.io/github/issues/juanjo78git/py6Nimmt.svg?style=flat-square
[badge-license]:http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[badge-pypi-version]:https://img.shields.io/pypi/v/py6Nimmt.svg?style=flat-square
[travis]:https://travis-ci.org/juanjo78git/py6Nimmt
[coveralls]:https://coveralls.io/github/juanjo78git/py6Nimmt
[issues]:https://github.com/juanjo78git/py6Nimmt/issues
[license]:LICENSE
[pypi]:https://pypi.python.org/pypi?:action=display&name=py6Nimmt
