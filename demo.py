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