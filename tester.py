# # --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import json

# Local
from bittrex_api.bittrex import Bittrex
from bittrex_api.v3 import BittrexV3

# ---------------------------------------------------------------------------------------------------------------------------------------- #

bittrex = BittrexV3(debug_level=3)

print(bittrex.ping())