from typing import Optional, Dict, List

from .utils.RequestManager import RequestManager

class BittrexV2:
    # set obj to True if want to use objects instead of jsons
    def __init__(
        self,
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        obj: bool = False,
        debug_level: int = 1
    ):
        self.requestUtils = RequestManager('https://bittrex.com/api/v2.0/', max_request_try_count = max_request_try_count, sleep_time = sleep_time, debug_level = debug_level)


    ############################################################ CURRENCIES ############################################################


    # returns btc price in USD
    def get_btc_price(self) -> Optional[float]:
        try:
            return self.requestUtils.get_resp(_EndPoints.GET_BTC_PRICE)['bpi']['USD']['rate_float']
        except:
            return None


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
    def get_currencies(self):
        return self.requestUtils.get_resp(_EndPoints.GET_CURRENCIES)


    ############################################################ MARKETS ############################################################


    # NOT WORKING
    # def get_markets(self):
    #     return self.requestUtils.get_resp(_EndPoints.GET_MARKETS)


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
    #     }
    # ]
    def get_market_summaries(self) -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_MARKET_SUMMARIES)


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
        return self.requestUtils.get_resp(_EndPoints.GET_MARKET_SUMMARY, params = {
            _KEYS.MARKET:market
        })


    ############################################################ MARKET ############################################################


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
    # 
    # tickInterval must be in ['oneMin', 'fiveMin', 'thirtyMin', 'hour', 'day']
    def get_ticks(self, market: str, interval: str = 'oneMin') -> Optional[List]:
        return self.requestUtils.get_resp(_EndPoints.GET_TICKS, params = {
            _KEYS.MARKET:market,
            _KEYS.TICK_INTERVAL:interval
        })


    # {
    #     "O": 0.01906712,
    #     "H": 0.01912402,
    #     "L": 0.01906712,
    #     "C": 0.01909821,
    #     "V": 61.52015402,
    #     "T": "2020-01-30T19:00:00",
    #     "BV": 1.17545776
    # }
    # tickInterval must be in ['oneMin', 'fiveMin', 'thirtyMin', 'hour', 'day']
    def get_latest_tick(self, market: str, interval: str = 'oneMin') -> Optional[Dict]:
        try:
            return self.requestUtils.get_resp(_EndPoints.GET_LATEST_TICK, params = {
                _KEYS.MARKET:market,
                _KEYS.TICK_INTERVAL:interval
            })[0]
        except:
            return None


class _EndPoints:
    # PUBLIC
        # CURRENCIES
        GET_BTC_PRICE  = 'pub/currencies/GetBTCPrice'
        GET_CURRENCIES = 'pub/currencies/GetCurrencies'

        # MARKETS
        GET_MARKETS          = 'pub/markets/GetMarkets'
        GET_MARKET_SUMMARIES = 'pub/markets/GetMarketSummaries'

        # MARKET
        GET_MARKET_SUMMARY   = 'pub/market/GetMarketSummary'
        GET_TICKS            = 'pub/market/GetTicks'
        GET_LATEST_TICK      = 'pub/market/GetLatestTick'


class _KEYS:
    MARKET        = 'marketName'
    TICK_INTERVAL = 'tickInterval'