# --------------------------------------------------------------- Imports --------------------------------------------------------------- #

# System
from enum import Enum

# --------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------- class: EndPoints ---------------------------------------------------------- #

class EndPoints(Enum):
    # Public
    GET_MARKETS             = 'public/getmarkets'
    GET_CURRENCIES          = 'public/getcurrencies'
    GET_TICKER              = 'public/getticker'
    GET_MARKET_SUMMARIES    = 'public/getmarketsummaries'
    GET_MARKET_SUMMARY      = 'public/getmarketsummary'
    GET_ORDER_BOOK          = 'public/getorderbook'
    GET_MARKET_HISTORY      = 'public/getmarkethistory'

    # Market
    BUY_LIMIT               = 'market/buylimit'
    SELL_LIMIT              = 'market/selllimit'
    CANCEL                  = 'market/cancel'
    GET_OPEN_ORDERS         = 'market/getopenorders'

    # Account
    GET_BALANCES            = 'account/getbalances'
    GET_BALANCE             = 'account/getbalance'
    GET_DEPOSIT_ADDRESS     = 'account/getdepositaddress'
    WITHDRAW                = 'account/withdraw'
    GET_ORDER               = 'account/getorder'
    GET_ORDER_HISTORY       = 'account/getorderhistory'
    GET_WITHDRAWAL_HISTORY  = 'account/getwithdrawalhistory'
    GET_DEPOSIT_HISTORY     = 'account/getdeposithistory'

# --------------------------------------------------------------------------------------------------------------------------------------- #