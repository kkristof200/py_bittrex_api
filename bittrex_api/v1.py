from typing import Optional, Dict, List

from .utils.RequestManager import RequestManager

class BittrexV1:
    # set obj to True if want to use objects instead of jsons
    def __init__(
        self,
        api_key: str = '',
        secret_key: str = '',
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        obj: bool = False,
        debug_level: int = 1
    ):
        self.requestUtils = RequestManager('https://api.bittrex.com/api/v1.1/', max_request_try_count = max_request_try_count, sleep_time = sleep_time, debug_level = debug_level)
        self.api_key = api_key
        self.secret_key = secret_key
        self.obj = obj

    ############################################################ PUBLIC ############################################################

    # [
    #     {
    #         "MarketCurrency": "LTC",
    #         "BaseCurrency": "BTC",
    #         "MarketCurrencyLong": "Litecoin",
    #         "BaseCurrencyLong": "Bitcoin",
    #         "MinTradeSize": 0.01,
    #         "MarketName": "BTC-LTC",
    #         "IsActive": true,
    #         "IsRestricted": false,
    #         "Created": "2014-02-13T00:00:00",
    #         "Notice": "BTC-LTC",
    #         "IsSponsored": false,
    #         "LogoUrl": "https://storage.blob.core.windows.net/public/8637ccad-9e7f-45ac-8f03-a41b440e3911.png"
    #     }
    # ]
    def get_markets(self) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_MARKETS)


    # [
    #     {
    #         "Currency": "BTC",
    #         "CurrencyLong": "Bitcoin",
    #         "CoinType": "BITCOIN",
    #         "MinConfirmation": 2,
    #         "TxFee": 0.002,
    #         "IsActive": true,
    #         "IsRestricted": false,
    #         "BaseAddress": null
    #     }
    # ]
    def get_currencies(self) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_CURRENCIES)
    

    # [
    #     {
    #         "MarketName": "BTC-LTC",
    #         "High": 0.0135,
    #         "Low": 0.012,
    #         "Volume": 3833.97619253,
    #         "Last": 0.01349998,
    #         "BaseVolume": 47.03987026,
    #         "TimeStamp": "2014-07-09T07:22:16.72",
    #         "Bid": 0.01271001,
    #         "Ask": 0.012911,
    #         "OpenBuyOrders": 45,
    #         "OpenSellOrders": 45,
    #         "PrevDay": 0.01229501,
    #         "Created": "2014-02-13T00:00:00",
    #         "DisplayMarketName": "string"
    #     }
    # ]
    def get_market_summaries(self) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_MARKET_SUMMARIES)
    

    # {
    #     "MarketName": "BTC-LTC",
    #     "High": 0.0135,
    #     "Low": 0.012,
    #     "Volume": 3833.97619253,
    #     "Last": 0.01349998,
    #     "BaseVolume": 47.03987026,
    #     "TimeStamp": "2014-07-09T07:22:16.72",
    #     "Bid": 0.01271001,
    #     "Ask": 0.012911,
    #     "OpenBuyOrders": 45,
    #     "OpenSellOrders": 45,
    #     "PrevDay": 0.01229501,
    #     "Created": "2014-02-13T00:00:00",
    #     "DisplayMarketName": "string"
    # }
    def get_market_summary(self, market: str) -> Optional[Dict]:
        summary_arr = self.requestUtils.get_resp(_EndPoints.GET_MARKET_SUMMARY, params = {
            _KEYS.MARKET:market
        })

        if summary_arr is not None and len(summary_arr) > 0:
            return summary_arr[0]
        
        return None
    

    # {
    #     "Bid": 2.05670368,
    #     "Ask": 3.35579531,
    #     "Last": 3.35579531
    # }
    def get_ticker(self, market: str) -> Optional[Dict]:
        return self.requestUtils.get_resp(_EndPoints.GET_TICKER, params = {
            _KEYS.MARKET:market
        })
    

    # {
    #     "buy": [
    #         {
    #             "quantity": 12.37,
    #             "rate": 32.55412402
    #         }
    #     ],
    #     "sell": [
    #         {
    #             "quantity": 12.37,
    #             "rate": 32.55412402
    #         }
    #     ]
    # }
    # 
    # type can be 'buy', 'sell', or 'both'
    def get_order_book(self, market: str, type: str = 'both') -> Optional[Dict]: # or Optional[List] if type != 'both'
        return self.requestUtils.get_resp(_EndPoints.GET_ORDER_BOOK, params = {
            _KEYS.MARKET:market,
            _KEYS.TYPE:type
        })
    

    # [
    #     {
    #         "Id": 319435,
    #         "TimeStamp": "2014-07-09T03:21:20.08",
    #         "Quantity": 0.30802438,
    #         "Price": 0.012634,
    #         "Total": 0.00389158,
    #         "FillType": "FILL",
    #         "OrderType": "BUY"
    #     }
    # ]
    def get_market_history(self, market: str) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_MARKET_HISTORY, params = {
            _KEYS.MARKET:market
        })


    ############################################################ MARKET ############################################################


    # "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def buy_limit(self, market: str, quantity: float, rate: float) -> Optional[str]:
        return self.__buy_sell(_EndPoints.BUY_LIMIT, market, quantity, rate)
    

    # "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def sell_limit(self, market: str, quantity: float, rate: float) -> Optional[str]:
        return self.__buy_sell(_EndPoints.SELL_LIMIT, market, quantity, rate)
    

    # True or False or None
    def cancel_order(self, uuid: str) -> Optional[bool]:
        return self.requestUtils.get_resp(_EndPoints.CANCEL, params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.UUID:uuid
        }, signature_key = self.secret_key)
    

    # [
    #     {
    #         "Uuid": null,
    #         "OrderUuid": "082a50b2-e21b-4a4c-8b20-90e5d8c1ef61",
    #         "Exchange": "BTC-CND",
    #         "OrderType": "LIMIT_SELL",
    #         "Quantity": 7836.27354484,
    #         "QuantityRemaining": 7836.27354484,
    #         "Limit": 6.8e-07,
    #         "CommissionPaid": 0.0,
    #         "Price": 0.0,
    #         "PricePerUnit": null,
    #         "Opened": "2020-02-27T17:18:47.18",
    #         "Closed": null,
    #         "CancelInitiated": false,
    #         "ImmediateOrCancel": false,
    #         "IsConditional": false,
    #         "Condition": "NONE",
    #         "ConditionTarget": null
    #     }
    # ]
    def get_open_orders(self, market: str = None) -> Optional[List]:
        params = {
            _KEYS.API_KEY:self.api_key
        }

        if market is not None:
            params[_KEYS.MARKET] = market

        return self.requestUtils.get_resp(_EndPoints.GET_OPEN_ORDERS, params, signature_key = self.secret_key)


    ############################################################ ACCOUNT ############################################################


    # [
    #     {
    #         "Currency": "DOGE",
    #         "Balance": 4.21549076,
    #         "Available": 4.21549076,
    #         "Pending": 0,
    #         "CryptoAddress": "DLxcEt3AatMyr2NTatzjsfHNoB9NT62HiF",
    #         "Requested": false,
    #         "Uuid": null
    #     }
    # ]
    def get_balances(self) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_BALANCES, params = {
            _KEYS.API_KEY:self.api_key
        }, signature_key = self.secret_key)
    

    # {
    #     "Currency": "DOGE",
    #     "Balance": 4.21549076,
    #     "Available": 4.21549076,
    #     "Pending": 0,
    #     "CryptoAddress": "DLxcEt3AatMyr2NTatzjsfHNoB9NT62HiF",
    #     "Requested": false,
    #     "Uuid": null
    # }
    def get_balance(self, currency: str) -> Optional[Dict]:
        return self.requestUtils.get_resp(_EndPoints.GET_BALANCE, params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.CURRENCY:currency
        }, signature_key = self.secret_key)
    

    # {
    #     "Currency": "VTC",
    #     "Address": "Vy5SKeKGXUHKS2WVpJ76HYuKAu3URastUo"
    # }
    def get_deposit_address(self, currency: str) -> Optional[Dict]:
        return self.requestUtils.get_resp(_EndPoints.GET_DEPOSIT_ADDRESS, params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.CURRENCY:currency
        }, signature_key = self.secret_key)
    

    # param address: the address where to send the funds
    # param paymentid: used for CryptoNotes/BitShareX/Nxt/XRP and any other coin that has a memo/message/tag/paymentid option
    # 
    # returns UUID: "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def withdraw(self, currency: str, quantity: float, address: str, payment_id: Optional[str] = None) -> Optional[str]:
        params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.CURRENCY:currency,
            _KEYS.ADDRESS:address
        }

        if payment_id is not None:
            params[_KEYS.PAYMENT_ID] = payment_id

        res = self.requestUtils.get_resp(_EndPoints.WITHDRAW, params = params, signature_key = self.secret_key)

        return self.__get_uuid(res)
    

    # {
    #     "AccountId": null,
    #     "OrderUuid": "082a50b2-e21b-4a4c-8b20-90e5d8c1ef61",
    #     "Exchange": "BTC-CND",
    #     "Type": "LIMIT_SELL",
    #     "Quantity": 7836.27354484,
    #     "QuantityRemaining": 7836.27354484,
    #     "Limit": 6.8e-07,
    #     "Reserved": null,
    #     "ReserveRemaining": null,
    #     "CommissionReserved": null,
    #     "CommissionReserveRemaining": null,
    #     "CommissionPaid": 0.0,
    #     "Price": 0.0,
    #     "PricePerUnit": null,
    #     "Opened": "2020-02-27T17:18:47.18",
    #     "Closed": null,
    #     "IsOpen": true,
    #     "Sentinel": null,
    #     "CancelInitiated": false,
    #     "ImmediateOrCancel": false,
    #     "IsConditional": false,
    #     "Condition": "NONE",
    #     "ConditionTarget": null
    # }
    def get_order(self, uuid: str) -> Optional[Dict]:
        return self.requestUtils.get_resp(_EndPoints.GET_ORDER, params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.UUID:uuid
        }, signature_key = self.secret_key)
    
    
    # [
    #     {
    #         "OrderUuid": "fd97d393-e9b9-4dd1-9dbf-f288fc72a185",
    #         "Exchange": "BTC-LTC",
    #         "TimeStamp": "string (date-time)",
    #         "OrderType": "string",
    #         "Limit": 1e-8,
    #         "Quantity": 667.03644955,
    #         "QuantityRemaining": 0,
    #         "Commission": 0.00004921,
    #         "Price": 0.01968424,
    #         "PricePerUnit": 0.0000295,
    #         "IsConditional": false,
    #         "Condition": "",
    #         "ConditionTarget": 0,
    #         "ImmediateOrCancel": false,
    #         "Closed": "2014-02-13T00:00:00"
    #     }
    # ]
    def get_order_history(self, market: Optional[str] = None) -> Optional[List]:
        params = {
            _KEYS.API_KEY:self.api_key
        }

        if market is not None:
            params[_KEYS.MARKET] = market

        return self.requestUtils.get_resp(_EndPoints.GET_ORDER_HISTORY, params, signature_key = self.secret_key)

    
    # [
    #     {
    #         "PaymentUuid": "b52c7a5c-90c6-4c6e-835c-e16df12708b1",
    #         "Currency": "BTC",
    #         "Amount": 17,
    #         "Address": "1DeaaFBdbB5nrHj87x3NHS4onvw1GPNyAu",
    #         "Opened": "2014-07-09T04:24:47.217",
    #         "Authorized": "boolean",
    #         "PendingPayment": "boolean",
    #         "TxCost": 0.0002,
    #         "TxId": "b4a575c2a71c7e56d02ab8e26bb1ef0a2f6cf2094f6ca2116476a569c1e84f6e",
    #         "Canceled": "boolean",
    #         "InvalidAddress": "boolean"
    #     }
    # ]
    def get_withdrawal_history(self, currency: Optional[str] = None) -> Optional[List]:
        params = {
            _KEYS.API_KEY:self.api_key
        }

        if currency is not None:
            params[_KEYS.CURRENCY] = currency

        return self.requestUtils.get_resp(_EndPoints.GET_WITHDRAWAL_HISTORY, params, signature_key = self.secret_key)

    
    # [
    #     {
    #         "Id": 1,
    #         "Amount": 2.12345678,
    #         "Currency": "BTC",
    #         "Confirmations": 2,
    #         "LastUpdated": "2014-02-13T07:38:53.883",
    #         "TxId": "e26d3b33fcfc2cb0c74d0938034956ea590339170bf4102f080eab4b85da9bde",
    #         "CryptoAddress": "15VyEAT4uf7ycrNWZVb1eGMzrs21BH95Va"
    #     }
    # ]
    def get_deposit_history(self, currency: Optional[str] = None) -> Optional[List]:
        params = {
            _KEYS.API_KEY:self.api_key
        }

        if currency is not None:
            params[_KEYS.CURRENCY] = currency

        return self.requestUtils.get_resp(_EndPoints.GET_DEPOSIT_HISTORY, params, signature_key = self.secret_key)


    ############################################################ UTILS ############################################################
    
    def __buy_sell(self, endpoint: str, market: str, quantity: float, rate: float) -> Optional[str]:
        res = self.requestUtils.get_resp(endpoint, params = {
            _KEYS.API_KEY:self.api_key,
            _KEYS.MARKET:market,
            _KEYS.QUANTITY:quantity,
            _KEYS.RATE:rate
        }, signature_key = self.secret_key)

        return self.__get_uuid(res)
    
    def __get_uuid(self, resp) -> Optional[str]:
        if resp is None:
            return None
        
        if self.obj and resp.uuid is not None:
            return resp.uuid
        elif not self.obj and 'uuid' in resp:
            return resp['uuid']
        
        return None

class _EndPoints:
    # PUBLIC
    GET_MARKETS          = 'public/getmarkets'
    GET_CURRENCIES       = 'public/getcurrencies'
    GET_TICKER           = 'public/getticker'
    GET_MARKET_SUMMARIES = 'public/getmarketsummaries'
    GET_MARKET_SUMMARY   = 'public/getmarketsummary'
    GET_ORDER_BOOK       = 'public/getorderbook'
    GET_MARKET_HISTORY   = 'public/getmarkethistory'

    # MARKET
    BUY_LIMIT       = 'market/buylimit'
    SELL_LIMIT      = 'market/selllimit'
    CANCEL          = 'market/cancel'
    GET_OPEN_ORDERS = 'market/getopenorders'

    # ACCOUNT
    GET_BALANCES           = 'account/getbalances'
    GET_BALANCE            = 'account/getbalance'
    GET_DEPOSIT_ADDRESS    = 'account/getdepositaddress'
    WITHDRAW               = 'account/withdraw'
    GET_ORDER              = 'account/getorder'
    GET_ORDER_HISTORY      = 'account/getorderhistory'
    GET_WITHDRAWAL_HISTORY = 'account/getwithdrawalhistory'
    GET_DEPOSIT_HISTORY    = 'account/getdeposithistory'


class _KEYS:
    MARKET     = 'market'
    TYPE       = 'type'
    QUANTITY   = 'quantity'
    RATE       = 'rate'
    API_KEY    = 'apikey'
    UUID       = 'uuid'
    CURRENCY   = 'currency'
    ADDRESS    = 'address'
    PAYMENT_ID = 'paymentid'