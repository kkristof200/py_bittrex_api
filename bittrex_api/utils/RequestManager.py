import time, hashlib, requests, hmac, os, json
from typing import Optional, Dict, Any

from .json2obj import j2o

class RequestManager:
    #   PUBLIC

    # set obj to True if want to use objects instead of jsons
    def __init__(
        self,
        base_url: str,
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        obj: bool = False,
        debug_level: int = 1
    ):
        self.base_url = base_url
        self.max_try_count = max_request_try_count
        self.sleep_time = max_request_try_count
        self.obj = obj
        self.debug_level = debug_level

    def get_resp(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        signature_key: Optional[str] = None
    ) -> Optional[Any]:
        current_try_count = 0

        while current_try_count < self.max_try_count:
            current_try_count += 1
            url = self.__create_url(endpoint, params)
            signature = None

            if signature_key is not None:
                signature = self.__generate_signarute(url, signature_key)

            r = self.__request(url, signature = signature)
            j = self.__get_resp_from_request(r)

            if j is not None:
                return j
            
            time.sleep(self.sleep_time)
        
        return None

    #   PRIVATE

    def __nonce(self):
        return str(int(time.time() * 1000))

    def __generate_signarute(self, message, salt):
        return hmac.new(salt.encode(), message.encode(), hashlib.sha512).hexdigest()

    def __create_url(self, endpoint, params = None):
        url = os.path.join(self.base_url, endpoint)

        if params is None:
            return url
        
        params['nonce'] = self.__nonce()
        i = 0

        for key, value in params.items():
            if i == 0:
                url += '?'
            else:
                url += '&'
            
            url += key + '=' +  str(value)
            i += 1
        
        return url

    def __request(self, url, signature = None):
        if self.debug_level >= 2:
            print(url)

        headers = {}

        if signature is not None:
            headers = {'apisign': signature}

        try:
            return requests.get(url, headers = headers)
        except requests.exceptions.RequestException as e:
            if self.debug_level >= 1:
                print(e)

            return None
    
    def __is_request_ok(self, r):
        if r is None:
            if self.debug_level >= 1:
                print('request is None')

            return False

        if r.status_code != 200:
            if self.debug_level >= 1:
                print(r)

            return False
        
        return True
    
    def __get_resp_from_request(self, r):
        if r is None:
            if self.debug_level >= 1:
                print('request is None')

            return None

        if r.status_code != 200:
            if self.debug_level >= 1:
                print(r)

            return None
        
        if self.debug_level >= 3:
            print(json.dumps(r.json(), indent=4))
        
        if self.obj:
            return self.__get_obj_from_response(r)
        else:
            return self.__get_json_from_request(r)

    def __get_json_from_request(self, r):
        json_data = r.json()

        if json_data is None:
            if self.debug_level >= 1:
                print('could not parse response into JSON')
                print(r)

            return None
        
        if 'success' not in json_data:
            if self.debug_level >= 1:
                print('does not have \'success\' field')

            return None

        if not json_data['success']:
            if self.debug_level >= 1:
                print('success is false')
                print(json.dumps(json_data, indent=4))

            return None
        
        if 'result' not in json_data or json_data['result'] is None:
            if self.debug_level >= 1:
                print('does not have \'result\' field or \'result\' is None')

            return True
        
        return json_data['result']

    def __get_obj_from_response(self, r):
        try:
            o = j2o(r.text)
        except:
            if self.debug_level >= 1:
                print('Exception while parsing response into object')

            return None

        if o is None:
            if self.debug_level >= 1:
                print('Got \'None\' from parsing response into object')

            return None

        if o.success is None:
            if self.debug_level >= 1:
                print('Object does not have \'success\' property')

            return None

        if o.success is False:
            if self.debug_level >= 1:
                msg = 'success property is false'

                if o.msg is not None:
                    msg = o.msg
                
                print(msg)

            return None

        if o.result is None:
            if self.debug_level >= 1:
                print('does not have \'result\' property')

            return True

        return o.result