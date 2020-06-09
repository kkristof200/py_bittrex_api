# --------------------------------------------------------------- Imports --------------------------------------------------------------- #

# System
from enum import Enum
import time, hashlib, requests, hmac, os, json, copy
from typing import Optional, Dict, List, Union, Any, Tuple

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

    # ------------------------------------------------------------- Init ------------------------------------------------------------ #

    def __init__(
        self,
        # base_url: str,
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        debug_level: int = 1
    ):
        # self.base_url = base_url.strip('/')
        self.max_try_count = max_request_try_count
        self.sleep_time = max_request_try_count
        self.debug_level = debug_level


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
                    data=data
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

    def __request(
        self,
        url: str,
        method: RequestMethod,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Optional[JSONData]:
        if self.debug_level >= 3:
            print(url)

        try:
            if method == RequestMethod.GET:
                resp = requests.get(url, params=params, headers=headers)
            elif method == RequestMethod.POST:
                resp = requests.post(url, data=data, params=params, headers=headers)
            else:#elif method == RequestMethod.DELETE:
                resp = requests.post(url, data=data, params=params, headers=headers)

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