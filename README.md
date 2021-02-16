# bittrex_api

![PyPI - version](https://img.shields.io/pypi/v/bittrex_api?style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/bittrex_api?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/bittrex_api?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/bittrex_api?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_bittrex_api?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_bittrex_api?style=flat-square) 

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_bittrex_api?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_bittrex_api?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_bittrex_api?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_bittrex_api?label=repo%20license&style=flat-square)

## Description

IMDB scraper

## Install

~~~~bash
pip install bittrex_api
# or
pip3 install bittrex_api
~~~~

## Usage
~~~~python
from bittrex_api import Bittrex


bittrex = Bittrex(
    api_key='',              # YOUR API KEY
    secret_key='',           # YOUR API SECRET
    max_request_try_count=3, # Max tries for a request to succeed
    sleep_time=2,            # sleep seconds between failed requests
    debug_level=3
)

v3 = bittrex.v3
# or
# from bittrex_api import *
# v3 = BittrexV3(
#     api_key='',              # YOUR API KEY
#     secret_key='',           # YOUR API SECRET
#     max_request_try_count=3, # Max tries for a request to succeed
#     sleep_time=2,            # sleep seconds between failed requests
#     debug_level=3,
#     reverse_market_names=True
# )

# V3 Usage samples
from kcu import kjson

MARKET_NAME = 'BTC-XRP'

kjson.print(v3.get_market(market=MARKET_NAME))
kjson.print(v3.get_market_summary(market=MARKET_NAME))
kjson.print(v3.get_orderbook(market=MARKET_NAME, depth=1))
~~~~

## Dependencies

[kcu](https://pypi.org/project/kcu), [requests](https://pypi.org/project/requests)