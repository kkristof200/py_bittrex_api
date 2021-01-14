# # --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Local
from bittrex_api.bittrex import Bittrex
from bittrex_api.v3 import *

# ---------------------------------------------------------------------------------------------------------------------------------------- #

# print(bittrex.post_order(bittrex.create_new_order_dict(
#     market='BTC-SC',
#     direction=OrderDirection.SELL,
#     type=OrderType.LIMIT,
#     time_in_force=TimeInForce.GOOD_TIL_CANCELLED,
#     quantity=3000,
#     limit=0.00000030
# )))


bittrex = BittrexV3(reverse_market_names=True, debug_level=3)

from kcu import kjson

# kjson.save('test1.json', bittrex.get_closed_orders())
# kjson.save('test2.json', bittrex.get_closed_orders(market='BTC-XRP'))
print(bittrex.get_orderbook(market='BTC-XRP', depth=1))