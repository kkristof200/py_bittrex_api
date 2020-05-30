# --------------------------------------------------------------- Imports ----------------------------------------------------------------#

# Local
from .v1 import BittrexV1
from .v2 import BittrexV2
from .v3 import BittrexV3

# ----------------------------------------------------------------------------------------------------------------------------------------#




# ------------------------------------------------------------ class: Bittrex ------------------------------------------------------------#

class Bittrex:

    # ------------------------------------------------------------- Init -------------------------------------------------------------#

    def __init__(
        self,
        api_key: str = '',
        secret_key: str = '',
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        debug_level: int = 1
    ):
        self.v1 = BittrexV1(api_key, secret_key, max_request_try_count, sleep_time, debug_level)
        self.v2 = BittrexV2(api_key, secret_key, max_request_try_count, sleep_time, debug_level)
        self.v3 = BittrexV3(api_key, secret_key, max_request_try_count, sleep_time, debug_level)

# ----------------------------------------------------------------------------------------------------------------------------------------#