# --------------------------------------------------------------- Imports --------------------------------------------------------------- #

# System
from typing import Optional, Dict, List, Union

# Local
from .__bittrex_core import BittrexCore
from .utils.bittrex_requests import BittrexRequests, RequestMethod, JSONData
from .models.v1.endpoints import EndPoints
from .models.v1.keys import Keys
from .models.v1 import order_book_type
from .utils.urls import Urls
from .utils import crypto

# --------------------------------------------------------------------------------------------------------------------------------------- #


OrderBookType = order_book_type.OrderBookType


# ----------------------------------------------------------- class: BittrexV1 ---------------------------------------------------------- #

class BittrexV1(BittrexCore):

    # ------------------------------------------------------ Private properties ------------------------------------------------------ #

    _base_url = 'https://api.bittrex.com/api/v1.1/'


    # -------------------------------------------------------- Public methods ------------------------------------------------------- #
    # ------------------------------------------------------------ Public ----------------------------------------------------------- #

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
        return self.__request(EndPoints.GET_MARKETS)


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
        return self.__request(EndPoints.GET_CURRENCIES)


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
        return self.__request(EndPoints.GET_MARKET_SUMMARIES)


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
        return self.__request(
            EndPoints.GET_MARKET_SUMMARY,
            params={
                Keys.MARKET:market
            },
            path=['result', 0]
        )

        # if summary_arr is not None and len(summary_arr) > 0:
        #     return summary_arr[0]
        
        # return None


    # {
    #     "Bid": 2.05670368,
    #     "Ask": 3.35579531,
    #     "Last": 3.35579531
    # }
    def get_ticker(self, market: str) -> Optional[Dict]:
        return self.__request(
            EndPoints.GET_TICKER,
            params={
                Keys.MARKET:market
            }
        )


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
    def get_order_book(
        self,
        market: str,
        type: OrderBookType = OrderBookType.BOTH
    ) -> Optional[Union[List, Dict]]: # or Optional[List] if type != OrderBookType.BOTH
        return self.__request(
            EndPoints.GET_ORDER_BOOK,
            params={
                Keys.MARKET:market,
                Keys.TYPE:type
            }
        )


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
        return self.__request(
            EndPoints.GET_MARKET_HISTORY,
            params={ Keys.MARKET:market }
        )


    # ------------------------------------------------------------ Market ----------------------------------------------------------- #

    # "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def buy(
        self,
        market: str,
        quantity: float,
        rate: float
    ) -> Optional[str]:
        return self.__buy_sell(
            EndPoints.BUY_LIMIT,
            market,
            quantity,
            rate
        )

    # Alias
    buy_limit = buy


    # "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def sell(
        self,
        market: str,
        quantity: float,
        rate: float
    ) -> Optional[str]:
        return self.__buy_sell(
            EndPoints.SELL_LIMIT,
            market,
            quantity,
            rate
        )

    # Alias
    sell_limit = sell


    # True or False or None
    def cancel(self, uuid: str) -> Optional[bool]:
        return self.__request(
            EndPoints.CANCEL,
            params={ Keys.UUID:uuid },
            path=['success'],
            signed=True
        )

    # Alias
    cancel_order = cancel


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
    def get_open_orders(self, market: Optional[str] = None) -> Optional[List]:
        params = None

        if market is not None:
            params = { Keys.MARKET:market }

        return self.__request(
            EndPoints.GET_OPEN_ORDERS,
            params=params,
            signed=True
        )


    # ----------------------------------------------------------- Account ----------------------------------------------------------- #

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
        return self.__request(
            EndPoints.GET_BALANCES,
            signed=True
        )


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
        return self.__request(
            EndPoints.GET_BALANCE,
            params={ Keys.CURRENCY:currency },
            signed=True
        )


    # {
    #     "Currency": "VTC",
    #     "Address": "Vy5SKeKGXUHKS2WVpJ76HYuKAu3URastUo"
    # }
    def get_deposit_address(self, currency: str) -> Optional[Dict]:
        return self.__request(
            EndPoints.GET_DEPOSIT_ADDRESS,
            params={ Keys.CURRENCY:currency },
            signed=True
        )


    # param address: the address where to send the funds
    # param paymentid: used for CryptoNotes/BitShareX/Nxt/XRP and any other coin that has a memo/message/tag/paymentid option
    # 
    # returns UUID: "614c34e4-8d71-11e3-94b5-425861b86ab6"
    def withdraw(self, currency: str, quantity: float, address: str, payment_id: Optional[str] = None) -> Optional[str]:
        params={
            Keys.CURRENCY:currency,
            Keys.ADDRESS:address
        }

        if payment_id is not None:
            params[Keys.PAYMENT_ID] = payment_id

        return self.__request(
            EndPoints.WITHDRAW,
            params=params,
            signed=True,
            path=['result', 'uuid']
        )


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
        return self.__request(
            EndPoints.GET_ORDER,
            params={ Keys.UUID:uuid },
            signed=True
        )

    
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
        params = None

        if market is not None:
            params = { Keys.MARKET:market }

        return self.__request(
            EndPoints.GET_ORDER_HISTORY,
            params=params,
            signed=True
        )

    
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
        params = None

        if currency is not None:
            params = { Keys.CURRENCY:currency }

        return self.__request(
            EndPoints.GET_WITHDRAWAL_HISTORY,
            params=params,
            signed=True
        )

    
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
        params = None

        if currency is not None:
            params = { Keys.CURRENCY:currency }

        return self.__request(
            EndPoints.GET_DEPOSIT_HISTORY,
            params=params,
            signed=True
        )


    # ------------------------------------------------------- Private methods ------------------------------------------------------- #

    def __request(
        self,
        endpoint: EndPoints,
        params: Optional[Dict] = None,
        signed: bool = False,
        path: Optional[List[str]] = None
    ) -> Optional[JSONData]:
        if signed:
            if params is None:
                params={}

            params[Keys.API_KEY] = self.api_key

        url = self.url_utils.url(endpoint.value, params)
        headers = None

        if signed:
            headers = {Keys.SIGNATURE: crypto.signature(url, self.api_secret)}

        return self.requests.request(
            url,
            RequestMethod.GET,
            headers=headers,
            needed_values={
                'success': True,
                'result': None
            },
            path=path or ['result']
        )

    def __buy_sell(self, endpoint: str, market: str, quantity: float, rate: float) -> Optional[str]:
        return self.__request(
            endpoint,
            params={
                Keys.API_KEY:self.api_key,
                Keys.MARKET:market,
                Keys.QUANTITY:quantity,
                Keys.RATE:rate
            },
            signed=True,
            path=['result', 'uuid']
        )


# ---------------------------------------------------------------------------------------------------------------------------------------- #