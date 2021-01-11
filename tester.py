# # --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Local
from bittrex_api.bittrex import Bittrex
from bittrex_api.v3 import *

# ---------------------------------------------------------------------------------------------------------------------------------------- #

# bittrex = BittrexV3('YOUR_API_KEY', 'YOUR_SECRET_KEY', debug_level=3, proxy=None)

# print(bittrex.post_order(bittrex.create_new_order_dict(
#     market='BTC-SC',
#     direction=OrderDirection.SELL,
#     type=OrderType.LIMIT,
#     time_in_force=TimeInForce.GOOD_TIL_CANCELLED,
#     quantity=3000,
#     limit=0.00000030
# )))


bittrex = BittrexV3(reverse_market_names=False, debug_level=3)

from kcu import kjson

kjson.save('test.json', bittrex.get_candles(market='BTC-USDT'))
# print(bittrex.get_orderbook(market='BTC-USDT', depth=1))