# --------------------------------------------------------------- Imports ----------------------------------------------------------------#

# System
from typing import Optional, Dict, Any

# Local
from . import strings

# ----------------------------------------------------------------------------------------------------------------------------------------#




# ------------------------------------------------------------- class: Urls --------------------------------------------------------------#

class Urls:

    # ------------------------------------------------------------- Init -------------------------------------------------------------#

    def __init__(
        self,
        base_url: str
    ):
        self.base_url = base_url.strip('/')


    # -------------------------------------------------------- Public methods --------------------------------------------------------#

    @staticmethod
    def join(*args) -> str:
        comps = []

        for arg in args:
            if arg is not None:
                comps.append(strings.to_string(arg).strip('/'))      
  
        return '/'.join(comps)


    def url(
        self,
        *endpoints_args,
        params: Optional[Dict] = None,
        use_nonce: bool = True
    ) -> str:
        endpoints_args = (self.base_url,) + endpoints_args
        url = self.join(*endpoints_args)

        if use_nonce and (params is None or 'nonce' not in params):
            if params is None:
                params = {}

            from . import crypto

            params['nonce'] = crypto.nonce()

        if params is None:
            return url

        to_append = ''

        for key, value in params.items():
            if value is None:
                continue

            if len(to_append) == 0:
                to_append += '?'
            else:
                to_append += '&'

            to_append += strings.to_string(key) + '=' +  strings.to_string(value)

        return url + to_append


# ----------------------------------------------------------------------------------------------------------------------------------------#