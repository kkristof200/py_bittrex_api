# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from enum import Enum

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: TimeInForce ---------------------------------------------------------- #

class TimeInForce(Enum):
    GOOD_TIL_CANCELLED              = 'GOOD_TIL_CANCELLED'
    IMMEDIATE_OR_CANCEL             = 'IMMEDIATE_OR_CANCEL'
    FILL_OR_KILL                    = 'FILL_OR_KILL'
    POST_ONLY_GOOD_TIL_CANCELLED    = 'POST_ONLY_GOOD_TIL_CANCELLED'
    BUY_NOW                         = 'BUY_NOW'

# ---------------------------------------------------------------------------------------------------------------------------------------- #