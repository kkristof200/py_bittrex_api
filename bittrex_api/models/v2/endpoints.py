# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from enum import Enum

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------- class: EndPoints ----------------------------------------------------------- #

class EndPoints(Enum):
    # Public
    # Currencies
    GET_BTC_PRICE        = 'pub/currencies/GetBTCPrice'
    GET_CURRENCIES       = 'pub/currencies/GetCurrencies'
    GET_CURRENCY_INFO    = 'pub/currencies/GetCurrencyInfo'
    WALLET_HEALTH        = 'pub/currencies/getwallethealth'

    # Markets
    GET_MARKETS          = 'pub/markets/GetMarkets'
    GET_MARKET_SUMMARIES = 'pub/markets/GetMarketSummaries'

    # Market
    GET_MARKET_SUMMARY   = 'pub/market/GetMarketSummary'
    GET_TICKS            = 'pub/market/GetTicks'
    GET_LATEST_TICK      = 'pub/market/GetLatestTick'

    # Auth
    # Trade
    BUY                  = 'auth/market/TradeBuy'
    SELL                 = 'auth/market/TradeSell'
    CANCEL_TRADE         = 'auth/market/TradeCancel'

    # Orders
    GET_ORDER_HISTORY    = 'auth/orders/GetOrderHistory'
# ---------------------------------------------------------------------------------------------------------------------------------------- #