from typing import Optional, Dict, List

from . import v1
from . import v2
from .utils.json2obj import j2o

import json

class BittrexAdditions:
    # set obj to True if want to use objects instead of jsons
    def __init__(
        self,
        max_request_try_count: int = 3,
        sleep_time: float = 7.5,
        obj: bool = False
    ):
        self.v1 = v1.BittrexV1(max_request_try_count = max_request_try_count, sleep_time = sleep_time, obj = False)
        self.v2 = v2.BittrexV2(max_request_try_count = max_request_try_count, sleep_time = sleep_time, obj = False)
        self.obj = obj


    ############################################################ CURRENCIES ############################################################

    # {
    #     "order_book": {
    #         "buy": [
    #             {
    #                 "Quantity": 0.26,
    #                 "Rate": 9660.35
    #             },
    #             ...
    #         ],
    #         "sell": [
    #             {
    #                 "Quantity": 0.07303041,
    #                 "Rate": 9663.363
    #             },
    #             ...
    #         ]
    #     },
    #     "summary": {
    #         "buy": 74.97747014000002,
    #         "sell": 97.58356915000005,
    #         "overall": -22.606099010000023,
    #         "overall_perc": 0.7683411335851922
    #     }
    # }
    def get_order_book_summary(self, market: str) -> Optional[Dict]:
        res = self.v1.get_order_book(market, 'both')

        if res is None:
            return None
        
        ext_res = {
            'order_book': res
        }

        total_buy = 0
        total_sell = 0

        if 'buy' in res:
            for e in res['buy']:
                total_buy += e['Quantity']
        
        if 'sell' in res:
            for e in res['sell']:
                total_sell += e['Quantity']

        total_sell_divider = total_sell

        if total_sell_divider == 0:
            total_sell_divider = 0.00000001

        ext_res['summary'] = {
            'buy': total_buy,
            'sell': total_sell,
            'overall': total_buy - total_sell,
            'overall_perc': total_buy / total_sell_divider
        }

        if self.obj:
            return j2o(json.dumps(ext_res))
        
        return ext_res

    # {
    #     "history": [
    #         {
    #             "Id": 66228541,
    #             "TimeStamp": "2020-05-19T17:43:37.5",
    #             "Quantity": 0.0014168,
    #             "Price": 9669.78,
    #             "Total": 13.700144304,
    #             "FillType": "FILL",
    #             "OrderType": "BUY",
    #             "Uuid": "4c3fade7-e2b1-4b61-90ae-9289c1b6a5de"
    #         },
    #         ...
    #     ],
    #     "summary": [
    #         "2020-05-19T18:03": {
    #             "buy": 1692.5292498180002,
    #             "sell": 891.8721905289,
    #             "total": 2584.4014403469,
    #             "sum": 800.6570592891002,
    #             "sum_perc": 1.8977262300490532
    #         },
    #         ...
    #     ]
    # }
    def get_market_history_summary(self, market: str) -> Optional[Dict]:
        res = self.v1.get_market_history(market)

        if res is None:
            return None
        
        ext_res = {
            'history': res,
            'summary': {}
        }

        last_time = None

        for e in reversed(res):
            new_time = e['TimeStamp'].rsplit(':', 1)[0]

            if new_time != last_time:
                ext_res['summary'][new_time] = {
                    'buy': 0,
                    'sell': 0,
                    'total': 0,
                    'sum': 0,
                    'sum_perc': 0
                }

            if e['OrderType'] == 'BUY':
                ext_res['summary'][new_time]['buy'] += e['Total']
            else:
                ext_res['summary'][new_time]['sell'] += e['Total']

            ext_res['summary'][new_time]['sum'] = ext_res['summary'][new_time]['buy'] - ext_res['summary'][new_time]['sell']
            ext_res['summary'][new_time]['total'] = ext_res['summary'][new_time]['buy'] + ext_res['summary'][new_time]['sell']

            sell_divider = ext_res['summary'][new_time]['sell']

            if sell_divider == 0:
                sell_divider = 0.00000001

            ext_res['summary'][new_time]['sum_perc'] = ext_res['summary'][new_time]['buy'] / sell_divider

            last_time = new_time
            
        return ext_res