# --------------------------------------------------------------- Imports --------------------------------------------------------------- #

# System
from enum import Enum

# --------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------- class: Keys ------------------------------------------------------------- #

class Keys(Enum):
    CURRENCY_SYMBOL   = 'currencySymbol'
    MARKET_SYMBOL = 'marketSymbol'

    NEXT_PAGE_TOKEN = 'nextPageToken'
    PREVIOUS_PAGE_TOKEN = 'previousPageToken'
    PAGE_SIZE = 'pageSize'
    START_DATE = 'startDate'
    END_DATE = 'endDate'

    OPERAND = 'operand'
    TRIGGER_PRICE = 'triggerPrice'
    TRAILING_STOP_PERCENT = 'trailingStopPercent'
    ORDER_TO_CREATE = 'orderToCreate'
    ORDER_TO_CANCEL = 'orderToCancel'
    CLIENT_CONDITIONAL_ORDER_ID = 'clientConditionalOrderId'

    ORDER_TYPE      = 'type'
    DIRECTION = 'direction'
    QUANTITY      = 'quantity'
    CEILING      = 'ceiling'
    LIMIT      = 'limit'
    TIME_IN_FORCE = 'timeInForce'
    CLIENT_ORDER_ID = 'clientOrderId'
    USE_AWARDS = 'useAwards'

    ID = 'id'
    DEPTH = 'depth'
    CANDLE_INTERVAL = 'candleInterval'

    STATUS = 'status'

    # MARKET          = 'marketName'
    # TICK_INTERVAL   = 'tickInterval'

    # ORDER_TYPE      = 'OrderType'
    # QUANTITY        = 'Quantity'
    # RATE            = 'Rate'
    # TIME_IN_EFFECT  = 'TimeInEffect'
    # CONDITION_TYPE  = 'ConditionType'
    # TARGET          = 'Target'

# --------------------------------------------------------------------------------------------------------------------------------------- #