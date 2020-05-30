# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Dict, List, Union

# Local
from .__bittrex_core import BittrexCore
from .utils.bittrex_requests import BittrexRequests, RequestMethod, JSONData
from .models.v2.endpoints import EndPoints
from .models.v2.keys import Keys
from .models.v2 import tick_interval, order_type, condition_type, time_in_effect
from .utils.urls import Urls
from .utils import crypto

# ---------------------------------------------------------------------------------------------------------------------------------------- #


TickInterval    = tick_interval.TickInterval
OrderType       = order_type.OrderType
ConditionType   = condition_type.ConditionType
TimeInEffect    = time_in_effect.TimeInEffect


# ----------------------------------------------------------- class: BittrexV2 ----------------------------------------------------------- #

class BittrexV2(BittrexCore):

    # ------------------------------------------------------ Private properties ------------------------------------------------------ #

    _base_url = 'https://bittrex.com/api/v2.0/'


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #
    # ------------------------------------------------------------ Public ------------------------------------------------------------ #

    # returns btc price in USD
    def get_btc_price(self) -> Optional[float]:
        self.__request(
            EndPoints.GET_BTC_PRICE,
            path=['result', 'bpi', 'USD', 'rate_float']
        )


    # [
    #     {
    #         "Currency": "BTC",
    #         "CurrencyLong": "Bitcoin",
    #         "MinConfirmation": 2,
    #         "TxFee": 0.00050000,
    #         "IsActive": true,
    #         "IsRestricted": false,
    #         "CoinType": "BITCOIN",
    #         "BaseAddress": "1N52wHoVR79PMDishab2XmRHsbekCdGquK",
    #         "Notice": null,
    #         "PermanentMessage": null
    #     }
    # ]
    def get_currencies(self) -> Optional[List]:
        return self.__request(EndPoints.GET_CURRENCIES)

    # {
    #     "Health": {
    #         "Currency": "BTC",
    #         "DepositQueueDepth": 0,
    #         "WithdrawQueueDepth": 3,
    #         "BlockHeight": 631759,
    #         "WalletBalance": 0.0,
    #         "WalletConnections": 8,
    #         "MinutesSinceBHUpdated": 2,
    #         "LastChecked": "2020-05-26T10:03:23.35",
    #         "IsActive": true
    #     },
    #     "Currency": "BTC",
    #     "CurrencyLong": "Bitcoin",
    #     "MinConfirmation": 2,
    #     "TxFee": 0.00050000,
    #     "IsActive": true,
    #     "IsRestricted": false,
    #     "CoinType": "BITCOIN",
    #     "BaseAddress": "1N52wHoVR79PMDishab2XmRHsbekCdGquK",
    #     "Notice": null,
    #     "PermanentMessage": null,
    #     "IsQuoteCurrency": true,
    #     "LogoUrl": "https://bittrexblobstorage.blob.core.windows.net/public/ddbdafb2-e267-4114-abc3-06316cf3bef9.png"
    # }
    def get_currency(self, currency: str) -> Optional[Dict]:
        return self.__request(
            EndPoints.GET_CURRENCY_INFO,
            params={
                Keys.CURRENCY_NAME:currency
            }
        )


    # [
    #     {
    #         "Health": {
    #             "Currency": "BTC",
    #             "DepositQueueDepth": 0,
    #             "WithdrawQueueDepth": 5,
    #             "BlockHeight": 631758,
    #             "WalletBalance": 0.0,
    #             "WalletConnections": 8,
    #             "MinutesSinceBHUpdated": 1,
    #             "LastChecked": "2020-05-26T09:54:07.14",
    #             "IsActive": true
    #         },
    #         "Currency": {
    #             "Currency": "BTC",
    #             "CurrencyLong": "Bitcoin",
    #             "MinConfirmation": 2,
    #             "TxFee": 0.00050000,
    #             "IsActive": true,
    #             "IsRestricted": false,
    #             "CoinType": "BITCOIN",
    #             "BaseAddress": "1N52wHoVR79PMDishab2XmRHsbekCdGquK",
    #             "Notice": null,
    #             "PermanentMessage": null,
    #             "IsQuoteCurrency": true,
    #             "LogoUrl": "https://bittrexblobstorage.blob.core.windows.net/public/ddbdafb2-e267-4114-abc3-06316cf3bef9.png"
    #         }
    #     },
    #     ...
    # ]
    def get_wallet_health(self) -> Optional[List]:
        return self.__request(EndPoints.WALLET_HEALTH)


    # NOT WORKING
    # def get_markets(self):
    #     return self.__request(EndPoints.GET_MARKETS)


    # [
    #     {
    #         "Market": {
    #             "MarketCurrency": "TRX",
    #             "BaseCurrency": "USD",
    #             "MarketCurrencyLong": "TRON",
    #             "BaseCurrencyLong": "US Dollar",
    #             "MinTradeSize": 135.19603425,
    #             "MarketName": "USD-TRX",
    #             "IsActive": true,
    #             "IsRestricted": false,
    #             "Created": "2018-09-17T22:23:27.547",
    #             "Notice": null,
    #             "IsSponsored": null,
    #             "LogoUrl": "https://bittrexblobstorage.blob.core.windows.net/public/8cd6f220-105c-464b-9862-0368d99d1379.png",
    #             "Leverage": null
    #         },
    #         "Summary": {
    #             "MarketName": "USD-TRX",
    #             "High": 0.01911000,
    #             "Low": 0.01780000,
    #             "Volume": 1394359.31129412,
    #             "Last": 0.01902000,
    #             "BaseVolume": 25869.46990021,
    #             "TimeStamp": "2020-01-30T19:04:08.52",
    #             "Bid": 0.01906000,
    #             "Ask": 0.01917000,
    #             "OpenBuyOrders": 108,
    #             "OpenSellOrders": 435,
    #             "PrevDay": 0.01885000,
    #             "Created": "2018-09-17T22:23:27.547",
    #             "Leverage": null
    #         },
    #         "IsVerified": false
    #     },
    #     ...
    # ]
    def get_market_summaries(self) -> Optional[List]:
        return self.__request(EndPoints.GET_MARKET_SUMMARIES)


    # {
    #     "MarketName": "BTC-ETH",
    #     "High": 0.01912360,
    #     "Low": 0.01851355,
    #     "Volume": 4814.77764798,
    #     "Last": 0.01910869,
    #     "BaseVolume": 90.55386914,
    #     "TimeStamp": "2020-01-30T19:07:28.513",
    #     "Bid": 0.01910869,
    #     "Ask": 0.01911280,
    #     "OpenBuyOrders": 978,
    #     "OpenSellOrders": 5114,
    #     "PrevDay": 0.01882325,
    #     "Created": "2015-08-14T09:02:24.817"
    # }
    def get_market_summary(self, market: str) -> Optional[Dict]:
        return self.__request(
            EndPoints.GET_MARKET_SUMMARY,
            params={
                Keys.MARKET:market
            }
        )


    # [
    #     {
    #         "O": 0.01775358,
    #         "H": 0.01776662,
    #         "L": 0.01774892,
    #         "C": 0.01775832,
    #         "V": 8.67420615,
    #         "T": "2019-12-21T19:00:00",
    #         "BV": 0.15404624
    #     }
    # ]
    def get_ticks(self, market: str, interval: TickInterval) -> Optional[List]:
        return self.__request(
            EndPoints.GET_TICKS,
            params={
                Keys.MARKET:market,
                Keys.TICK_INTERVAL:interval
            }
        )


    # {
    #     "O": 0.01906712,
    #     "H": 0.01912402,
    #     "L": 0.01906712,
    #     "C": 0.01909821,
    #     "V": 61.52015402,
    #     "T": "2020-01-30T19:00:00",
    #     "BV": 1.17545776
    # }
    def get_latest_tick(self, market: str, interval: TickInterval) -> Optional[Dict]:
        return self.__request(
            EndPoints.GET_LATEST_TICK,
            params={
                Keys.MARKET:market,
                Keys.TICK_INTERVAL:interval
            },
            path=['result', 0]
        )


    # ------------------------------------------------------------- Auth ------------------------------------------------------------- #

    # {
    #     BuyOrSell: "Buy",
    #     MarketCurrency: "DGB",
    #     MarketName: "BTC-DGB",
    #     OrderId: "cb31d615-91eb-408f-87c3-b35b7d751817",
    #     OrderType: "LIMIT",
    #     Quantity: 49875,
    #     Rate:1e-8
    # }
    def buy(
        self,
        market: str,
        quantity:float,
        rate:float,
        type: OrderType,
        time_in_effect: TimeInEffect,
        condition_type: ConditionType,
        target: int = 0
    ) -> Optional[Dict]:
        return self.__buy_sell(
            EndPoints.BUY,
            market,
            quantity,
            rate,
            type,
            time_in_effect,
            condition_type,
            target
        )


    # {
    #     BuyOrSell: "Sell",
    #     MarketCurrency: "DGB",
    #     MarketName: "BTC-DGB",
    #     OrderId: "cb31d615-91eb-408f-87c3-b35b7d751817",
    #     OrderType: "LIMIT",
    #     Quantity: 49875,
    #     Rate:1e-8
    # }
    def sell(
        self,
        market: str,
        quantity:float,
        rate:float,
        type: OrderType,
        time_in_effect: TimeInEffect,
        condition_type: ConditionType,
        target: int = 0
    ) -> Optional[Dict]:
        return self.__buy_sell(
            EndPoints.SELL,
            market,
            quantity,
            rate,
            type,
            time_in_effect,
            condition_type,
            target
        )


    # True or False or None
    def cancel(self, uuid: str) -> Optional[bool]:
        return self.__request(
            EndPoints.CANCEL_TRADE,
            params={
                Keys.UUID:uuid
            },
            path=['success'],
            signed=True
        )

    # Alias
    cancel_order = cancel


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    def __buy_sell(
        self,
        endpoint: EndPoints,
        market: str,
        quantity:float,
        rate:float,
        type: OrderType,
        time_in_effect: TimeInEffect,
        condition_type: ConditionType,
        target: int
    ) -> Optional[Dict]:
        return self.__request(
            endpoint,
            params={
                Keys.MARKET:market,
                Keys.QUANTITY:quantity,
                Keys.RATE:rate,
                Keys.ORDER_TYPE:type,
                Keys.TIME_IN_EFFECT:time_in_effect,
                Keys.CONDITION_TYPE:condition_type,
                Keys.TARGET:target,
            },
            signed=True
        )

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

        url = self.url_utils.url(endpoint.value, params=params)
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


# ---------------------------------------------------------------------------------------------------------------------------------------- #