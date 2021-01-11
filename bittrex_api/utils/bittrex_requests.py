# --------------------------------------------------------------- Imports --------------------------------------------------------------- #

# System
from enum import Enum
import time, hashlib, requests, hmac, os, json, copy
from typing import Optional, Dict, List, Union, Any, Tuple
from .strings import to_string

# --------------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------------- Defines --------------------------------------------------------------- #

JSONData = Union[
    str, int, float, bool,
    Dict[str, Any],
    List[Any],
    Tuple[Any]
]

class RequestMethod(Enum):
    GET     = 'GET'
    POST    = 'POST'
    DELETE  = 'DELETE'

# --------------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: BittrexRequests ------------------------------------------------------- #

class BittrexRequests:
    __USAGE_INTERVAL         = 60
    __MAX_USAGE_PER_INTERVAL = 20

    # ------------------------------------------------------------- Init ------------------------------------------------------------ #

    def __init__(
        self,
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        debug_level: int = 1,
        proxy: Optional[Union[List, str]] = None
    ):
        self.max_try_count = max_request_try_count
        self.sleep_time = max_request_try_count
        self.debug_level = debug_level

        if type(proxy) == str:
            proxy = [proxy]

        self.proxies = proxy
        self.proxy_history = {}


    # -------------------------------------------------------- Public methods ------------------------------------------------------- #

    def request(
        self,
        url: str,
        method: RequestMethod,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        data: Optional[Dict] = None,
        needed_values: Optional[Dict] = None,
        unwanted_values: Optional[Dict] = None,
        path: Optional[List] = None
    ) -> Optional[JSONData]:
        current_try_count = 0

        while current_try_count < self.max_try_count:
            current_try_count += 1

            j = self.__sub_json(
                self.__request(
                    url,
                    method,
                    params=params,
                    headers=headers,
                    json_data=data
                ),
                needed_values=needed_values,
                unwanted_values=unwanted_values,
                path=path
            )

            if j is not None:
                return j
            
            time.sleep(self.sleep_time)
        
        return None


    # ------------------------------------------------------- Private methods ------------------------------------------------------- #

    def __get_proxy(self) -> Optional[str]:
        if not self.proxies:
            return None

        self.__normalize_proxy_history()

        for proxy in self.proxies:
            self.proxy_history[proxy] = self.proxy_history[proxy] if proxy in self.proxy_history else []

            if len(self.proxy_history[proxy]) < self.__MAX_USAGE_PER_INTERVAL:
                return proxy.lstrip('https://').lstrip('http://').lstrip('ftp://')

        return None

    def __normalize_proxy_history(self) -> None:
        now = int(time.time())

        for proxy in list(self.proxy_history.keys()):
            if len(self.proxy_history[proxy]) < self.__MAX_USAGE_PER_INTERVAL:
                continue

            self.proxy_history[proxy] = [ts for ts in self.proxy_history[proxy] if now - ts < self.__USAGE_INTERVAL]

    def __request(
        self,
        url: str,
        method: RequestMethod,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        json_data: Optional[Dict] = None
    ) -> Optional[JSONData]:
        if self.debug_level >= 3:
            print(url)

        if params:
            params = {to_string(k):to_string(v) for k, v in params.items() if v}

        try:
            proxy = self.__get_proxy()
            proxies = {
                'http':  'http://{}'.format(proxy),
                'https': 'https://{}'.format(proxy),
                'ftp':   'ftp://{}'.format(proxy)
            } if proxy else None

            if proxy:
                self.proxy_history[proxy] = self.proxy_history[proxy] if proxy in self.proxy_history else []
                self.proxy_history[proxy].append(int(time.time()))

            if method == RequestMethod.GET:
                resp = requests.get(url, params=params, headers=headers, proxies=proxies)
            elif method == RequestMethod.POST:
                resp = requests.post(url, json=json_data, params=params, headers=headers, proxies=proxies)
            else:#elif method == RequestMethod.DELETE:
                resp = requests.delete(url, json=json_data, params=params, headers=headers, proxies=proxies)

            if resp is None:
                if self.debug_level >= 1:
                    print('Response is None')
            elif resp.status_code not in [200, 201]:
                if self.debug_level >= 1:
                    print(resp.status_code, resp.text)

                return None

            return resp.json()
        except requests.exceptions.RequestException as e:
            if self.debug_level >= 1:
                print(e)

            return None
    
    def __sub_json(
        self,
        j: Optional[JSONData],
        needed_values: Optional[Dict],
        unwanted_values: Optional[Dict],
        path: Optional[List]
    ) -> Optional[JSONData]:
        if j is None:
            return None
        
        if needed_values is not None:
            for k, v in needed_values.items():
                if k not in j:
                    if self.debug_level >= 1:
                        print(k, 'not found in response')

                    if self.debug_level >= 2:
                        print(json.dumps(j, indent=4))

                    return None

                # if j[k] is None:
                #     if self.debug_level >= 1:
                #         print(k, 'is None')

                #     if self.debug_level >= 2:
                #         print(json.dumps(j, indent=4))

                #     return None

                if v is not None and j[k] != v:
                    if self.debug_level >= 1:
                        print('\'' + k + '\': ', j[k], '- is not', v)

                    if self.debug_level >= 2:
                        print(json.dumps(j, indent=4))

                    return None
        
        if unwanted_values is not None:
            for value in unwanted_values:
                if value in j:
                    if self.debug_level >= 1:
                        print('found unwanted value \'' + value + '\' in response')

                    if self.debug_level >= 2:
                        print(json.dumps(j, indent=4))

                    return None
        
        if path is None:
            return j

        full_j = copy.deepcopy(j)

        try:
            for k in path:
                j = j[k]
        except Exception as e:
            if self.debug_level >= 1:
                print(e)

            if self.debug_level >= 2:
                print(json.dumps(full_j, indent=4))

            return None

        return j


# --------------------------------------------------------------------------------------------------------------------------------------- #