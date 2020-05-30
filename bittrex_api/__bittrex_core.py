# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from abc import ABCMeta, abstractmethod

# Local
from .utils.bittrex_requests import BittrexRequests
from .utils.urls import Urls

# ---------------------------------------------------------------------------------------------------------------------------------------- #




# ---------------------------------------------------------- class: BittrexCore ---------------------------------------------------------- #

class BittrexCore:#(ABCMeta):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        api_key: str = '',
        api_secret: str = '',
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        debug_level: int = 1
    ):
        self.url_utils = Urls(
            base_url=self._base_url
        )
        self.requests = BittrexRequests(
            max_request_try_count=max_request_try_count,
            sleep_time=sleep_time,
            debug_level=debug_level
        )
        self.api_key = api_key
        self.api_secret = api_secret

    # ------------------------------------------------------ Private properties ------------------------------------------------------ #

    @property
    @abstractmethod
    def _base_url(self):
        """The url to append the endpoints to"""


# ---------------------------------------------------------------------------------------------------------------------------------------- #