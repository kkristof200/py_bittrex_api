# # --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Local
from bittrex_api.bittrex import Bittrex
from bittrex_api.v3 import *

# ---------------------------------------------------------------------------------------------------------------------------------------- #

bittrex = BittrexV3('YOUR_API_KEY', 'YOUR_SECRET_KEY', debug_level=3)

print(bittrex.post_order(bittrex.create_new_order_dict(
    market='SC-BTC',
    direction=OrderDirection.SELL,
    type=OrderType.LIMIT,
    time_in_force=TimeInForce.GOOD_TIL_CANCELLED,
    quantity=3000,
    limit=0.00000030
)))