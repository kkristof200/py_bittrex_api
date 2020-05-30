# --------------------------------------------------------------- Imports ----------------------------------------------------------------#

# System
from enum import Enum

# ----------------------------------------------------------------------------------------------------------------------------------------#



# ----------------------------------------------------------- class: EndPoints ---------------------------------------------------------- #

class EndPoints(Enum):
    # Public


    # Auth
    ACCOUNT         = 'account' # GET
    ACCOUNT_VOLUME         = 'account/volume' # GET
    ADDRESSES         = 'addresses' # GET, POST
    BALANCES = 'balances'
    CONDITIONAL_ORDERS = 'conditional-orders'
    CLOSED = 'closed'
    OPEN = 'open'
    DEPOSITS = 'deposits'
    BY_TX_ID = 'ByTxId'

    WITHDRAWALS = 'withdrawals'
    ORDERS = 'orders'


    # Public
    PING = 'ping'
    CURRENCIES = 'currencies'
    MARKETS = 'markets'
    SUMMARIES = 'summaries'
    TICKERS = 'tickers'
    TICKER = 'ticker'
    ORDER_BOOK = 'orderbook'
    TRADES = 'trades'
    CANDLES = 'candles'
    RECENT = 'recent'
    HISTORICAL = 'historical'

# ----------------------------------------------------------------------------------------------------------------------------------------#