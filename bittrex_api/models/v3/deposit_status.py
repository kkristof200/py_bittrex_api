# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from enum import Enum

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: DepositStatus --------------------------------------------------------- #

class DepositStatus(Enum):
    PENDING     = 'PENDING'
    COMPLETED   = 'COMPLETED'
    ORPHANED    = 'ORPHANED'
    INVALIDATED = 'INVALIDATED'

# ---------------------------------------------------------------------------------------------------------------------------------------- #