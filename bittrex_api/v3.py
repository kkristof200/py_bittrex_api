# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Dict, List

# Local
from .__bittrex_core import BittrexCore
from .utils.bittrex_requests import BittrexRequests, RequestMethod, JSONData
from .models.v3.endpoints import EndPoints
from .models.v3.keys import Keys
from .models.v3 import conditional_order_operand, time_in_force, order_direction, order_type, cancel_order_type, candle_interval, deposit_status, withdrawal_status
# from .models.common.request_method import RequestMethod
from .utils.urls import Urls
from .utils import enums

# ---------------------------------------------------------------------------------------------------------------------------------------- #

ConditionalOrderOperand = conditional_order_operand.ConditionalOrderOperand
TimeInForce             = time_in_force.TimeInForce
OrderDirection          = order_direction.OrderDirection
OrderType               = order_type.OrderType
CancelOrderType         = cancel_order_type.CancelOrderType
CandleInterval          = candle_interval.CandleInterval
DepositStatus           = deposit_status.DepositStatus
WithdrawalStatus        = withdrawal_status.WithdrawalStatus

# ----------------------------------------------------------- class: BittrexV3 ----------------------------------------------------------- #

class BittrexV3(BittrexCore):

    # ------------------------------------------------------ Private properties ------------------------------------------------------ #

    _base_url = 'https://api.bittrex.com/v3/'
    REVERSE_MARKET_NAMES = True


    # -------------------------------------------------------- Public methods -------------------------------------------------------- #
    # ------------------------------------------------------------- Ping ------------------------------------------------------------- #

    # Response:
    # {
    #     "serverTime": "integer (int64)"
    # }
    def ping(self) -> Optional[Dict]:
        """Pings the service

        Returns:
            Optional[List[Dict]] -- ServicePing
        """

        return self.__request(
            EndPoints.PING,
            method=RequestMethod.GET
        )


    # ---------------------------------------------------------- Currencies ---------------------------------------------------------- #

    # Response:
    # [
    #     {
    #         "symbol": "string",
    #         "name": "string",
    #         "coinType": "string",
    #         "status": "string",
    #         "minConfirmations": "integer (int32)",
    #         "notice": "string",
    #         "txFee": "number (double)",
    #         "logoUrl": "string",
    #         "prohibitedIn": [
    #            "string"
    #         ]
    #     }
    # ]
    def get_curencies(self) -> Optional[List[Dict]]:
        """List currencies.

        Returns:
            Optional[List[Dict]] -- List of currencies
        """

        return self.__request(
            EndPoints.CURRENCIES,
            method=RequestMethod.GET
        )

    # Response:
    # {
    #     "symbol": "string",
    #     "name": "string",
    #     "coinType": "string",
    #     "status": "string",
    #     "minConfirmations": "integer (int32)",
    #     "notice": "string",
    #     "txFee": "number (double)",
    #     "logoUrl": "string",
    #     "prohibitedIn": [
    #         "string"
    #     ]
    # }
    def get_curency(self, currency: str) -> Optional[Dict]:
        """Retrieve info on a specified currency.

        Arguments:
            currency {str} -- symbol of the currency to retrieve

        Returns:
            Optional[Dict] -- Currency
        """

        return self.__request(
            EndPoints.CURRENCIES, currency,
            method=RequestMethod.GET
        )


    # ----------------------------------------------------------- Markets ------------------------------------------------------------ #

    # Response:
    # [
    #     {
    #         "symbol": "string",
    #         "baseCurrencySymbol": "string",
    #         "quoteCurrencySymbol": "string",
    #         "minTradeSize": "number (double)",
    #         "precision": "integer (int32)",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "notice": "string",
    #         "prohibitedIn": [
    #             "string"
    #         ]
    #     }
    # ]
    def get_markets(self) -> Optional[List[Dict]]:
        """List markets.

        Returns:
            Optional[List[Dict]] -- List of Market infos
        """

        return self.__request(
            EndPoints.MARKETS,
            method=RequestMethod.GET
        )

    # Response:
    # {
    #     "symbol": "string",
    #     "baseCurrencySymbol": "string",
    #     "quoteCurrencySymbol": "string",
    #     "minTradeSize": "number (double)",
    #     "precision": "integer (int32)",
    #     "status": "string",
    #     "createdAt": "string (date-time)",
    #     "notice": "string",
    #     "prohibitedIn": [
    #         "string"
    #     ]
    # }
    def get_market(self, market: str) -> Optional[Dict]:
        """Retrieve information for a specific market.

        Arguments:
            market {str} -- symbol of market to retrieve info for

        Returns:
            Optional[Dict] -- Market info
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market),
            method=RequestMethod.GET
        )

    # Response:
    # [
    #     {
    #         "symbol": "string",
    #         "high": "number (double)",
    #         "low": "number (double)",
    #         "volume": "number (double)",
    #         "baseVolume": "number (double)",
    #         "quoteVolume": "number (double)",
    #         "percentChange": "number (double)",
    #         "updatedAt": "string (date-time)"
    #     }
    # ]
    def get_market_summaries(self) -> Optional[List[Dict]]:
        """List summaries of the last 24 hours of activity for all markets. ** Note: baseVolume is being deprecated and will be removed in favor of quoteVolume

        Returns:
            Optional[List[Dict]] -- List of Market summaries
        """

        return self.__request(
            EndPoints.MARKETS, EndPoints.SUMMARIES,
            method=RequestMethod.GET
        )

    # Response:
    # {
    #     "symbol": "string",
    #     "high": "number (double)",
    #     "low": "number (double)",
    #     "volume": "number (double)",
    #     "baseVolume": "number (double)",
    #     "quoteVolume": "number (double)",
    #     "percentChange": "number (double)",
    #     "updatedAt": "string (date-time)"
    # }
    def get_market_summary(self, market: str) -> Optional[Dict]:
        """Retrieve summary of the last 24 hours of activity for a specific market. ** Note: baseVolume is being deprecated and will be removed in favor of quoteVolume

        Arguments:
            market {str} -- symbol of market to retrieve summary for

        Returns:
            Optional[Dict] -- Market summary
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market),
            method=RequestMethod.GET
        )

    # Response:
    # [
    #     {
    #         "symbol": "string",
    #         "lastTradeRate": "number (double)",
    #         "bidRate": "number (double)",
    #         "askRate": "number (double)"
    #     }
    # ]
    def get_tickers(self) -> Optional[List[Dict]]:
        """List tickers for all markets.

        Returns:
            Optional[List[Dict]] -- List of Tickers
        """

        return self.__request(
            EndPoints.MARKETS, EndPoints.TICKERS,
            method=RequestMethod.GET
        )

    # Response:
    # {
    #     "symbol": "string",
    #     "lastTradeRate": "number (double)",
    #     "bidRate": "number (double)",
    #     "askRate": "number (double)"
    # }
    def get_ticker(self, market: str) -> Optional[Dict]:
        """Retrieve the ticker for a specific market.

        Arguments:
            market {str} -- symbol of market to retrieve ticker for

        Returns:
            Optional[Dict] -- Ticker
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.TICKER,
            method=RequestMethod.GET
        )

    # Response:
    # {
    #     "bid": [
    #         {
    #             "quantity": "number (double)",
    #             "rate": "number (double)"
    #         }
    #     ],
    #     "ask": [
    #         {
    #             "quantity": "number (double)",
    #             "rate": "number (double)"
    #         }
    #     ]
    # }
    def get_orderbook(
        self,
        market: str,
        depth: Optional[int] = None
    ) -> Optional[Dict]:
        """Retrieve the ticker for a specific market.

        Arguments:
            market {str} -- symbol of market to retrieve order book for

        Keyword Arguments:
            depth {Optional[int]} -- maximum depth of order book to return (optional, allowed values are [1, 25, 500], default is 25) (default: {None})

        Returns:
            Optional[Dict] -- OrderBook
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.ORDER_BOOK,
            method=RequestMethod.GET,
            params={
                Keys.DEPTH:depth
            }
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "executedAt": "string (date-time)",
    #         "quantity": "number (double)",
    #         "rate": "number (double)",
    #         "takerSide": "string"
    #     }
    # ]
    def get_trades(
        self,
        market: str
    ) -> Optional[List[Dict]]:
        """Retrieve the recent trades for a specific market

        Arguments:
            market {str} -- symbol of market to retrieve trades for

        Returns:
            Optional[Dict] -- List of trades
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.TRADES,
            method=RequestMethod.GET
        )

    # Response:
    # [
    #     {
    #         "startsAt": "string (date-time)",
    #         "open": "number (double)",
    #         "high": "number (double)",
    #         "low": "number (double)",
    #         "close": "number (double)",
    #         "volume": "number (double)",
    #         "baseVolume": "number (double)",
    #         "quoteVolume": "number (double)"
    #     }
    # ]
    def get_candles(
        self,
        market: str,
        candle_interval: Optional[CandleInterval] = None
    ) -> Optional[List[Dict]]:
        """Retrieve recent candles for a specific market. The maximum age of the returned candles depends on the interval as follows: (MINUTE_1: 1 day, MINUTE_5: 1 day, HOUR_1: 31 days, DAY_1: 366 days). Candles for intervals without any trading activity are omitted. ** Note: baseVolume is being deprecated and will be removed in favor of quoteVolume

        Arguments:
            market {str} -- symbol of market to retrieve candles for

        Keyword Arguments:
            candle_interval {Optional[CandleInterval]} -- desired time interval between candles (default: {None})

        Returns:
            Optional[List[Dict]] -- List of candles
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.CANDLES,
            method=RequestMethod.GET,
            params={
                Keys.CANDLE_INTERVAL:candle_interval
            }
        )

    # Response:
    # [
    #     {
    #         "startsAt": "string (date-time)",
    #         "open": "number (double)",
    #         "high": "number (double)",
    #         "low": "number (double)",
    #         "close": "number (double)",
    #         "volume": "number (double)",
    #         "baseVolume": "number (double)",
    #         "quoteVolume": "number (double)"
    #     }
    # ]
    def get_recent_candles(
        self,
        market: str,
        candle_interval: CandleInterval
    ) -> Optional[List[Dict]]:
        """Retrieve recent candles for a specific market and candle interval. The maximum age of the returned candles depends on the interval as follows: (MINUTE_1: 1 day, MINUTE_5: 1 day, HOUR_1: 31 days, DAY_1: 366 days). Candles for intervals without any trading activity are omitted. ** Note: baseVolume is being deprecated and will be removed in favor of quoteVolume

        Arguments:
            market {str} -- symbol of market to retrieve candles for

            candle_interval {CandleInterval} -- desired time interval between candles

        Returns:
            Optional[List[Dict]] -- List of candles
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.CANDLES, candle_interval.value ,EndPoints.RECENT,
            method=RequestMethod.GET
        )

    # Response:
    # [
    #     {
    #         "startsAt": "string (date-time)",
    #         "open": "number (double)",
    #         "high": "number (double)",
    #         "low": "number (double)",
    #         "close": "number (double)",
    #         "volume": "number (double)",
    #         "baseVolume": "number (double)",
    #         "quoteVolume": "number (double)"
    #     }
    # ]
    def get_historical_candles(
        self,
        market: str,
        candle_interval: CandleInterval,
        year: int,
        month: Optional[int],
        day: Optional[int],
    ) -> Optional[List[Dict]]:
        """Retrieve recent candles for a specific market and candle interval. The date range of returned candles depends on the interval as follows: (MINUTE_1: 1 day, MINUTE_5: 1 day, HOUR_1: 31 days, DAY_1: 366 days). Candles for intervals without any trading activity are omitted. ** Note: baseVolume is being deprecated and will be removed in favor of quoteVolume

        Arguments:
            market {str} -- symbol of market to retrieve candles for

            candle_interval {CandleInterval} -- desired time interval between candles

            year {int} -- desired year to start from

            month {int} -- desired month to start from (if applicable)

            day {int} -- desired day to start from (if applicable)

        Returns:
            Optional[List[Dict]] -- List of candles
        """

        return self.__request(
            EndPoints.MARKETS, self.__optionally_reversed_market_name(market), EndPoints.CANDLES, candle_interval.value ,EndPoints.HISTORICAL, year, month, day,
            method=RequestMethod.GET
        )


    # --------------------------------------------------------- Auth methods --------------------------------------------------------- #
    # ------------------------------------------------------------ Account ----------------------------------------------------------- #

    # Response:
    # {
    #     "subaccountId": "string (uuid)",
    #     "accountId": "string (uuid)"
    # }
    def get_account(self) -> Optional[Dict]:
        """Retrieve information for the account associated with the request. For now, it only echoes the subaccount if one was specified in the header, which can be used to verify that one is operating on the intended account. More fields will be added later.

        Returns:
            Optional[Dict] -- Account
        """

        return self.__request(
            EndPoints.ACCOUNT,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "updated": "string (date-time)",
    #     "volume30days": "number (double)"
    # }
    def get_account_volume(self) -> Optional[Dict]:
        """Get 30 day volume for account

        Returns:
            Optional[Dict] -- AccountVolume
        """        
        return self.__request(
            EndPoints.ACCOUNT_VOLUME,
            method=RequestMethod.GET,
            signed=True
        )


    # ----------------------------------------------------------- Addresses ---------------------------------------------------------- #

    # Response:
    # [
    #     {
    #         "status": "string",
    #         "currencySymbol": "string",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string"
    #     }
    # ]
    def get_addresses(self) -> Optional[List[Dict]]:
        """List deposit addresses that have been requested or provisioned.

        Returns:
            Optional[List[Dict]] -- List of Addresses
        """        
        return self.__request(
            EndPoints.ADDRESSES,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "status": "string",
    #     "currencySymbol": "string",
    #     "cryptoAddress": "string",
    #     "cryptoAddressTag": "string"
    # }
    def get_address(self, currency: str) -> Optional[Dict]:
        """Retrieve the status of the deposit address for a particular currency for which one has been requested or provisioned.

        Arguments:
            currency {str} -- the currency ID to provision a new address for

        Returns:
            Optional[Dict] -- Address
        """

        return self.__request(
            EndPoints.ADDRESSES, currency,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "status": "string",
    #     "currencySymbol": "string",
    #     "cryptoAddress": "string",
    #     "cryptoAddressTag": "string"
    # }
    def create_address(self, currency: str) -> Optional[Dict]:
        """Retrieve the status of the deposit address for a particular currency for which one has been requested or provisioned.

        Arguments:
            currency {str} -- symbol of the currency to retrieve the deposit address for

        Returns:
            Optional[Dict] -- Address
        """

        return self.__request(
            EndPoints.ADDRESSES,
            method=RequestMethod.POST,
            body={
                Keys.CURRENCY_SYMBOL:currency
            },
            signed=True
        )


    # ----------------------------------------------------------- Balances ----------------------------------------------------------- #

    # Response:
    # [
    #     {
    #         "currencySymbol": "string",
    #         "total": "number (double)",
    #         "available": "number (double)",
    #         "updatedAt": "string (date-time)"
    #     }
    # ]
    def get_balances(self) -> Optional[List[Dict]]:
        """List account balances across available currencies. Returns a Balance entry for each currency for which there is either a balance or an address.

        Returns:
            Optional[List[Dict]] -- List of Balances
        """

        return self.__request(
            EndPoints.BALANCES,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "currencySymbol": "string",
    #     "total": "number (double)",
    #     "available": "number (double)",
    #     "updatedAt": "string (date-time)"
    # }
    def get_balance(self, curency: str) -> Optional[Dict]:
        """Retrieve account balance for a specific currency. Request will always succeed when the currency exists, regardless of whether there is a balance or address.

        Arguments:
            curency {str} -- unique symbol of the currency to retrieve the account balance for

        Returns:
            Optional[Dict] -- Balance
        """

        return self.__request(
            EndPoints.BALANCES, curency,
            method=RequestMethod.GET,
            signed=True
        )


    # ----------------------------------------------------------- Deposits ----------------------------------------------------------- #

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txId": "string",
    #         "confirmations": "integer (int32)",
    #         "updatedAt": "string (date-time)",
    #         "completedAt": "string (date-time)",
    #         "status": "string",
    #         "source": "string"
    #     }
    # ]
    def get_open_deposits(
        self,
        status: Optional[DepositStatus] = None,
        currency: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List open deposits. Results are sorted in inverse order of UpdatedAt, and are limited to the first 1000.

        Arguments:
            curency {str} -- unique symbol of the currency to retrieve the account balance for

        Keyword Arguments:
            status {Optional[DepositStatus]} -- filter by an open deposit status (optional). Only accepted non-null value by Bittrex is PENDING (default: {None})

            currency {Optional[str]} -- filter by currency (optional) (default: {None})

        Returns:
            Optional[List[Dict]] -- List of deposits
        """

        return self.__request(
            EndPoints.DEPOSITS, EndPoints.OPEN,
            method=RequestMethod.GET,
            params={
                Keys.STATUS:status,
                Keys.CURRENCY_SYMBOL:currency,
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txId": "string",
    #         "confirmations": "integer (int32)",
    #         "updatedAt": "string (date-time)",
    #         "completedAt": "string (date-time)",
    #         "status": "string",
    #         "source": "string"
    #     }
    # ]
    def get_closed_deposits(
        self,
        status: Optional[DepositStatus] = None,
        currency: Optional[str] = None,
        next_page_token: Optional[str] = None,
        previous_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List closed deposits. StartDate and EndDate filters apply to the CompletedAt field. Pagination and the sort order of the results are in inverse order of the CompletedAt field.

        Keyword Arguments:
            status {Optional[DepositStatus]} -- filter by an open deposit status. Only accepted non-null values by Bittrex are [COMPLETED, ORPHANED, INVALIDATED] (optional) (default: {None})

            currency {Optional[str]} -- filter by currency (optional) (default: {None})

            next_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should start after, in the sort order of the given endpoint. Used for traversing a paginated set in the forward direction. (Optional. May only be specified if PreviousPageToken is not specified.) (default: {None})

            previous_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should end before, in the sort order of the given endpoint. Used for traversing a paginated set in the reverse direction. (Optional. May only be specified if NextPageToken is not specified.) (default: {None})

            page_size {Optional[str]} -- maximum number of items to retrieve - default 100, minimum 1, maximum 200 (optional) (default: {None})

            start_date {Optional[str]} -- (optional) Filters out results before this timestamp. In ISO 8601 format (e.g., "2019-01-02T16:23:45Z"). Precision beyond one second is not supported. Use pagination parameters for more precise filtering. (default: {None})

            end_date {Optional[str]} -- (optional) Filters out result after this timestamp. Uses the same format as StartDate. Either, both, or neither of StartDate and EndDate can be set. The only constraint on the pair is that, if both are set, then EndDate cannot be before StartDate. (default: {None})

        Returns:
            Optional[List[Dict]] -- List of deposits
        """

        return self.__request(
            EndPoints.DEPOSITS, EndPoints.CLOSED,
            method=RequestMethod.GET,
            params={
                Keys.STATUS:status,
                Keys.CURRENCY_SYMBOL:currency,
                Keys.NEXT_PAGE_TOKEN:next_page_token,
                Keys.PREVIOUS_PAGE_TOKEN:previous_page_token,
                Keys.PAGE_SIZE:page_size,
                Keys.START_DATE:start_date,
                Keys.END_DATE:end_date
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txId": "string",
    #         "confirmations": "integer (int32)",
    #         "updatedAt": "string (date-time)",
    #         "completedAt": "string (date-time)",
    #         "status": "string",
    #         "source": "string"
    #     }
    # ]
    def get_deposits_by_tx_id(
        self,
        tx_id: str
    ) -> Optional[List[Dict]]:
        """List open deposits. Results are sorted in inverse order of UpdatedAt, and are limited to the first 1000.

        Arguments:
            tx_id {str} -- the transaction id to lookup

            currency {Optional[str]} -- filter by currency (optional) (default: {None})

        Returns:
            Optional[List[Dict]] -- List of deposits
        """

        return self.__request(
            EndPoints.DEPOSITS, EndPoints.BY_TX_ID, tx_id,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "currencySymbol": "string",
    #     "quantity": "number (double)",
    #     "cryptoAddress": "string",
    #     "cryptoAddressTag": "string",
    #     "txId": "string",
    #     "confirmations": "integer (int32)",
    #     "updatedAt": "string (date-time)",
    #     "completedAt": "string (date-time)",
    #     "status": "string",
    #     "source": "string"
    # }
    def get_deposits_by_deposit_id(
        self,
        deposit_id: str
    ) -> Optional[Dict]:
        """List open deposits. Results are sorted in inverse order of UpdatedAt, and are limited to the first 1000.

        Arguments:
            deposit_id {str} -- (uuid-formatted string) - ID of the deposit to retrieve

        Returns:
            Optional[Dict] -- Deposit
        """

        return self.__request(
            EndPoints.DEPOSITS, deposit_id,
            method=RequestMethod.GET,
            signed=True
        )


    # ---------------------------------------------------------- Withdrawals --------------------------------------------------------- #

    # Response:s
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txCost": "number (double)",
    #         "txId": "string",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "completedAt": "string (date-time)"
    #     }
    # ]
    def get_open_withdrawals(
        self,
        status: Optional[WithdrawalStatus] = None,
        currency: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List open withdrawals. Results are sorted in inverse order of the CreatedAt field, and are limited to the first 1000.

        Keyword Arguments:
            status {Optional[WithdrawalStatus]} -- ACCEPTED VALUES IF NOT NONE: [REQUESTED, AUTHORIZED, PENDING, ERROR_INVALID_ADDRESS]. Filter by an open withdrawal status (optional)

            currency {Optional[str]} -- filter by currency (optional)

        Returns:
            Optional[List[Dict]] -- List of Withdrawals
        """

        return self.__request(
            EndPoints.WITHDRAWALS, EndPoints.OPEN,
            method=RequestMethod.GET,
            params={
                Keys.STATUS:status,
                Keys.CURRENCY_SYMBOL:currency
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txCost": "number (double)",
    #         "txId": "string",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "completedAt": "string (date-time)"
    #     }
    # ]
    def get_closed_withdrawals(
        self,
        status: Optional[WithdrawalStatus] = None,
        currency: Optional[str] = None,
        next_page_token: Optional[str] = None,
        previous_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List open withdrawals. Results are sorted in inverse order of the CreatedAt field, and are limited to the first 1000.

        Keyword Arguments:
            status {Optional[WithdrawalStatus]} -- ACCEPTED VALUES IF NOT NONE: [COMPLETED, CANCELLED]. Filter by an open withdrawal status (optional)

            currency {Optional[str]} -- filter by currency (optional)

            next_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should start after, in the sort order of the given endpoint. Used for traversing a paginated set in the forward direction. (Optional. May only be specified if PreviousPageToken is not specified.) (default: {None})

            previous_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should end before, in the sort order of the given endpoint. Used for traversing a paginated set in the reverse direction. (Optional. May only be specified if NextPageToken is not specified.) (default: {None})

            page_size {Optional[str]} -- maximum number of items to retrieve - default 100, minimum 1, maximum 200 (optional) (default: {None})

            start_date {Optional[str]} -- (optional) Filters out results before this timestamp. In ISO 8601 format (e.g., "2019-01-02T16:23:45Z"). Precision beyond one second is not supported. Use pagination parameters for more precise filtering. (default: {None})

            end_date {Optional[str]} -- (optional) Filters out result after this timestamp. Uses the same format as StartDate. Either, both, or neither of StartDate and EndDate can be set. The only constraint on the pair is that, if both are set, then EndDate cannot be before StartDate. (default: {None})

        Returns:
            Optional[List[Dict]] -- List of withdrawals
        """

        return self.__request(
            EndPoints.WITHDRAWALS, EndPoints.CLOSED,
            method=RequestMethod.GET,
            params={
                Keys.STATUS:status,
                Keys.CURRENCY_SYMBOL:currency,
                Keys.NEXT_PAGE_TOKEN:next_page_token,
                Keys.PREVIOUS_PAGE_TOKEN:previous_page_token,
                Keys.PAGE_SIZE:page_size,
                Keys.START_DATE:start_date,
                Keys.END_DATE:end_date
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "currencySymbol": "string",
    #         "quantity": "number (double)",
    #         "cryptoAddress": "string",
    #         "cryptoAddressTag": "string",
    #         "txCost": "number (double)",
    #         "txId": "string",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "completedAt": "string (date-time)"
    #     }
    # ]
    def get_withdrawals_by_tx_id(
        self,
        tx_id: str
    ) -> Optional[List[Dict]]:
        """Retrieves all withdrawals for this account with the given TxId

        Arguments:
            tx_id {str} -- the transaction id to lookup

        Returns:
            Optional[List[Dict]] -- List of withdrawals
        """

        return self.__request(
            EndPoints.WITHDRAWALS, EndPoints.BY_TX_ID, tx_id,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "currencySymbol": "string",
    #     "quantity": "number (double)",
    #     "cryptoAddress": "string",
    #     "cryptoAddressTag": "string",
    #     "txCost": "number (double)",
    #     "txId": "string",
    #     "status": "string",
    #     "createdAt": "string (date-time)",
    #     "completedAt": "string (date-time)"
    # }
    def get_deposits_by_withdrawal_id(
        self,
        withdrawal_id: str
    ) -> Optional[Dict]:
        """Retrieve information on a specified withdrawal.

        Arguments:
            withdrawal_id {str} -- (uuid-formatted string) - ID of the withdrawal to retrieve

        Returns:
            Optional[Dict] -- Withdrawal
        """

        return self.__request(
            EndPoints.WITHDRAWALS, withdrawal_id,
            method=RequestMethod.GET,
            signed=True
        )


    # ------------------------------------------------------------ Orders ------------------------------------------------------------ #

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "limit": "number (double)",
    #         "ceiling": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "fillQuantity": "number (double)",
    #         "commission": "number (double)",
    #         "proceeds": "number (double)",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "updatedAt": "string (date-time)",
    #         "closedAt": "string (date-time)",
    #         "orderToCancel": {
    #             "type": "string",
    #             "id": "string (uuid)"
    #         }
    #     }
    # ]
    def get_open_orders(
        self,
        market: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List open orders.

        Keyword Arguments:
            market {Optional[str]} -- filter by market (optional)

        Returns:
            Optional[List[Dict]] -- List of orders
        """

        return self.__request(
            EndPoints.ORDERS, EndPoints.OPEN,
            method=RequestMethod.GET,
            params={
                Keys.MARKET_SYMBOL:market
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "limit": "number (double)",
    #         "ceiling": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "fillQuantity": "number (double)",
    #         "commission": "number (double)",
    #         "proceeds": "number (double)",
    #         "status": "string",
    #         "createdAt": "string (date-time)",
    #         "updatedAt": "string (date-time)",
    #         "closedAt": "string (date-time)",
    #         "orderToCancel": {
    #             "type": "string",
    #             "id": "string (uuid)"
    #         }
    #     }
    # ]
    def get_closed_orders(
        self,
        market: Optional[str] = None,
        next_page_token: Optional[str] = None,
        previous_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List closed orders. StartDate and EndDate filters apply to the ClosedAt field. Pagination and the sort order of the results are in inverse order of the ClosedAt field.

        Keyword Arguments:
            market {Optional[str]} -- filter by market (optional)

            next_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should start after, in the sort order of the given endpoint. Used for traversing a paginated set in the forward direction. (Optional. May only be specified if PreviousPageToken is not specified.) (default: {None})

            previous_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should end before, in the sort order of the given endpoint. Used for traversing a paginated set in the reverse direction. (Optional. May only be specified if NextPageToken is not specified.) (default: {None})

            page_size {Optional[str]} -- maximum number of items to retrieve - default 100, minimum 1, maximum 200 (optional) (default: {None})

            start_date {Optional[str]} -- (optional) Filters out results before this timestamp. In ISO 8601 format (e.g., "2019-01-02T16:23:45Z"). Precision beyond one second is not supported. Use pagination parameters for more precise filtering. (default: {None})

            end_date {Optional[str]} -- (optional) Filters out result after this timestamp. Uses the same format as StartDate. Either, both, or neither of StartDate and EndDate can be set. The only constraint on the pair is that, if both are set, then EndDate cannot be before StartDate. (default: {None})

        Returns:
            Optional[List[Dict]] -- List of orders
        """

        return self.__request(
            EndPoints.ORDERS, EndPoints.CLOSED,
            method=RequestMethod.GET,
            params={
                Keys.MARKET_SYMBOL:market,
                Keys.NEXT_PAGE_TOKEN:next_page_token,
                Keys.PREVIOUS_PAGE_TOKEN:previous_page_token,
                Keys.PAGE_SIZE:page_size,
                Keys.START_DATE:start_date,
                Keys.END_DATE:end_date
            },
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "marketSymbol": "string",
    #     "direction": "string",
    #     "type": "string",
    #     "quantity": "number (double)",
    #     "limit": "number (double)",
    #     "ceiling": "number (double)",
    #     "timeInForce": "string",
    #     "clientOrderId": "string (uuid)",
    #     "fillQuantity": "number (double)",
    #     "commission": "number (double)",
    #     "proceeds": "number (double)",
    #     "status": "string",
    #     "createdAt": "string (date-time)",
    #     "updatedAt": "string (date-time)",
    #     "closedAt": "string (date-time)",
    #     "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #     }
    # }
    def get_order_by_id(
        self,
        order_id: str
    ) -> Optional[Dict]:
        """Retrieve information on a specific order.

        Arguments:
            order_id {str} -- (uuid-formatted string) - ID of order to retrieve

        Returns:
            Optional[Dict] -- Order
        """

        return self.__request(
            EndPoints.ORDERS, order_id,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "marketSymbol": "string",
    #     "direction": "string",
    #     "type": "string",
    #     "quantity": "number (double)",
    #     "limit": "number (double)",
    #     "ceiling": "number (double)",
    #     "timeInForce": "string",
    #     "clientOrderId": "string (uuid)",
    #     "fillQuantity": "number (double)",
    #     "commission": "number (double)",
    #     "proceeds": "number (double)",
    #     "status": "string",
    #     "createdAt": "string (date-time)",
    #     "updatedAt": "string (date-time)",
    #     "closedAt": "string (date-time)",
    #     "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #     }
    # }
    def cancel_order(
        self,
        order_id: str
    ) -> Optional[Dict]:
        """Cancel an order.

        Arguments:
            order_id {str} -- (uuid-formatted string) - ID of order to cancel

        Returns:
            Optional[Dict] -- Order
        """

        return self.__request(
            EndPoints.ORDERS, order_id,
            method=RequestMethod.DELETE,
            signed=True
        )
    
    def post_order(
        self,
        order_dict: Dict
    ):
        """Cancel an order.

        Arguments:
            order_dict {str} -- (CHECK: 'create_new_order_dict') | order to create

        Returns:
            Optional[Dict] -- Order
        """

        return self.__request(
            EndPoints.ORDERS,
            method=RequestMethod.POST,
            body=order_dict,
            signed=True
        )


    # ------------------------------------------------------ Conditional Orders ------------------------------------------------------ #

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "marketSymbol": "string",
    #     "operand": "string",
    #     "triggerPrice": "number (double)",
    #     "trailingStopPercent": "number (double)",
    #     "createdOrderId": "string (uuid)",
    #     "orderToCreate": {
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "ceiling": "number (double)",
    #         "limit": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "useAwards": "boolean"
    #     },
    #     "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #     },
    #     "clientConditionalOrderId": "string (uuid)",
    #     "status": "string",
    #     "orderCreationErrorCode": "string",
    #     "createdAt": "string (date-time)",
    #     "updatedAt": "string (date-time)",
    #     "closedAt": "string (date-time)"
    # }
    def get_conditional_order(self, uuid: str) -> Optional[Dict]:
        """Retrieve information on a specific conditional order.

        Arguments:
            uuid {str} -- (uuid-formatted string) - ID of conditional order to retrieve

        Returns:
            Optional[Dict] -- ConditionalOrder
        """

        return self.__request(
            EndPoints.CONDITIONAL_ORDERS, uuid,
            method=RequestMethod.GET,
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "marketSymbol": "string",
    #     "operand": "string",
    #     "triggerPrice": "number (double)",
    #     "trailingStopPercent": "number (double)",
    #     "createdOrderId": "string (uuid)",
    #     "orderToCreate": {
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "ceiling": "number (double)",
    #         "limit": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "useAwards": "boolean"
    #     },
    #     "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #     },
    #     "clientConditionalOrderId": "string (uuid)",
    #     "status": "string",
    #     "orderCreationErrorCode": "string",
    #     "createdAt": "string (date-time)",
    #     "updatedAt": "string (date-time)",
    #     "closedAt": "string (date-time)"
    # }
    def cancel_conditional_order(self, uuid: str) -> Optional[Dict]:
        """Cancel a conditional order.

        Arguments:
            uuid {str} -- (uuid-formatted string) - ID of order to cancel

        Returns:
            Optional[Dict] -- ConditionalOrder
        """

        return self.__request(
            EndPoints.CONDITIONAL_ORDERS, uuid,
            method=RequestMethod.DELETE,
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "marketSymbol": "string",
    #         "operand": "string",
    #         "triggerPrice": "number (double)",
    #         "trailingStopPercent": "number (double)",
    #         "createdOrderId": "string (uuid)",
    #         "orderToCreate": {
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "ceiling": "number (double)",
    #         "limit": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "useAwards": "boolean"
    #         },
    #         "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #         },
    #         "clientConditionalOrderId": "string (uuid)",
    #         "status": "string",
    #         "orderCreationErrorCode": "string",
    #         "createdAt": "string (date-time)",
    #         "updatedAt": "string (date-time)",
    #         "closedAt": "string (date-time)"
    #     }
    # ]
    def get_closed_conditional_orders(
        self,
        market: Optional[str] = None,
        next_page_token: Optional[str] = None,
        previous_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Optional[List[Dict]]:
        """List closed conditional orders. StartDate and EndDate filters apply to the ClosedAt field. Pagination and the sort order of the results are in inverse order of the ClosedAt field.

        Keyword Arguments:
            market {Optional[str]} -- filter by market (optional) (default: {None})

            next_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should start after, in the sort order of the given endpoint. Used for traversing a paginated set in the forward direction. (Optional. May only be specified if PreviousPageToken is not specified.) (default: {None})

            previous_page_token {Optional[str]} -- The unique identifier of the item that the resulting query result should end before, in the sort order of the given endpoint. Used for traversing a paginated set in the reverse direction. (Optional. May only be specified if NextPageToken is not specified.) (default: {None})

            page_size {Optional[int]} -- maximum number of items to retrieve - default 100, minimum 1, maximum 200 (optional) (default: {None})

            start_date {Optional[str]} -- (optional) Filters out results before this timestamp. In ISO 8601 format (e.g., "2019-01-02T16:23:45Z"). Precision beyond one second is not supported. Use pagination parameters for more precise filtering. (default: {None})

            end_date {Optional[str]} -- (optional) Filters out result after this timestamp. Uses the same format as StartDate. Either, both, or neither of StartDate and EndDate can be set. The only constraint on the pair is that, if both are set, then EndDate cannot be before StartDate. (default: {None})

        Returns:
            Optional[List[Dict]] -- List of ConditionalOrders
        """

        return self.__request(
            EndPoints.CONDITIONAL_ORDERS, EndPoints.CLOSED,
            method=RequestMethod.GET,
            params={
                Keys.MARKET_SYMBOL:self.__optionally_reversed_market_name(market),
                Keys.NEXT_PAGE_TOKEN:next_page_token,
                Keys.PREVIOUS_PAGE_TOKEN:previous_page_token,
                Keys.PAGE_SIZE:page_size,
                Keys.START_DATE:start_date,
                Keys.END_DATE:end_date
            },
            signed=True
        )

    # Response:
    # [
    #     {
    #         "id": "string (uuid)",
    #         "marketSymbol": "string",
    #         "operand": "string",
    #         "triggerPrice": "number (double)",
    #         "trailingStopPercent": "number (double)",
    #         "createdOrderId": "string (uuid)",
    #         "orderToCreate": {
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "ceiling": "number (double)",
    #         "limit": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "useAwards": "boolean"
    #         },
    #         "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #         },
    #         "clientConditionalOrderId": "string (uuid)",
    #         "status": "string",
    #         "orderCreationErrorCode": "string",
    #         "createdAt": "string (date-time)",
    #         "updatedAt": "string (date-time)",
    #         "closedAt": "string (date-time)"
    #     }
    # ]
    def get_open_conditional_orders(self, market: Optional[str]) -> Optional[List[Dict]]:
        """List open conditional orders.

        Arguments:
            market {Optional[str]} -- filter by market (optional)

        Returns:
            Optional[List[Dict]] -- List of ConditionalOrders
        """

        return self.__request(
            EndPoints.CONDITIONAL_ORDERS, EndPoints.OPEN,
            method=RequestMethod.GET,
            params={
                Keys.MARKET_SYMBOL:self.__optionally_reversed_market_name(market)
            },
            signed=True
        )

    # Response:
    # {
    #     "id": "string (uuid)",
    #     "marketSymbol": "string",
    #     "operand": "string",
    #     "triggerPrice": "number (double)",
    #     "trailingStopPercent": "number (double)",
    #     "createdOrderId": "string (uuid)",
    #     "orderToCreate": {
    #         "marketSymbol": "string",
    #         "direction": "string",
    #         "type": "string",
    #         "quantity": "number (double)",
    #         "ceiling": "number (double)",
    #         "limit": "number (double)",
    #         "timeInForce": "string",
    #         "clientOrderId": "string (uuid)",
    #         "useAwards": "boolean"
    #     },
    #     "orderToCancel": {
    #         "type": "string",
    #         "id": "string (uuid)"
    #     },
    #     "clientConditionalOrderId": "string (uuid)",
    #     "status": "string",
    #     "orderCreationErrorCode": "string",
    #     "createdAt": "string (date-time)",
    #     "updatedAt": "string (date-time)",
    #     "closedAt": "string (date-time)"
    # }
    def create_conditional_order(
        self,
        market: str,
        order_to_create: Dict,
        order_to_cancel: Dict,
        operand: Optional[ConditionalOrderOperand] = None,
        trigger_price: Optional[float] = None,
        trailing_stop_percent: Optional[float] = None,
        client_conditional_order_id: Optional[str] = None
    ) -> Optional[Dict]:
        """Create a new conditional order

        Arguments:
            market {str} -- unique symbol of the market this conditional order will be tracking

            order_to_create {Dict} -- (CHECK: 'create_new_order_dict') | order to create if this conditional order is triggered
            
            order_to_cancel {Dict} -- (CHECK: 'create_new_cancel_order_dict') | order or conditional order to cancel if this conditional order triggers Note that this relationship is reciprocal.

        Keyword Arguments:
            operand {Optional[ConditionalOrderOperand]} -- price above (GTE) or below (LTE) which the conditional order will trigger This value will be set automatically if trailingStopPercent is specified. (either this or trailingStopPercent must be specified) (default: {None})

            trigger_price {Optional[float]} -- percent above the minimum price (GTE) or below the maximum price (LTE) at which to trigger (either this or trailing_stop_percent must be specified) (default: {None})

            trailing_stop_percent {Optional[float]} -- the stop price will automatically adjust relative to the most extreme trade value seen. (either this or trigger price must be specified) (default: {None})

            client_conditional_order_id {Optional[str]} -- [description] (default: {None})

        Returns:
            Optional[Dict] -- NewConditionalOrder
        """

        return self.__request(
            EndPoints.CONDITIONAL_ORDERS,
            method=RequestMethod.POST,
            body={
                Keys.MARKET_SYMBOL:self.__optionally_reversed_market_name(market),
                Keys.OPERAND:operand,
                Keys.TRIGGER_PRICE:trigger_price,
                Keys.TRAILING_STOP_PERCENT: trailing_stop_percent,
                Keys.ORDER_TO_CREATE: order_to_create,
                Keys.ORDER_TO_CANCEL: order_to_cancel,
                Keys.CLIENT_CONDITIONAL_ORDER_ID: client_conditional_order_id
            },
            signed=True
        )


    # ------------------------------------------------------- Helper methods --------------------------------------------------------- #

    def create_new_order_dict(
        self,
        market: str,
        direction: OrderDirection,
        type: OrderType,
        time_in_force: TimeInForce,
        quantity: Optional[float] = None,
        ceiling: Optional[float] = None,
        limit: Optional[float] = None,
        client_order_id: Optional[str] = None,
        use_awards: Optional[bool] = None
    ) -> Dict:
        """order to create

        Arguments:
            market {str} -- unique symbol of the market this order is being placed on

            direction {OrderDirection} -- order direction

            type {OrderType} -- order type

            time_in_force {TimeInForce} -- time in force

        Keyword Arguments:
            quantity {Optional[float]} -- quantity (optional, must be included for non-ceiling orders and excluded for ceiling orders) (default: {None})

            ceiling {Optional[float]} -- must be included for ceiling orders and excluded for non-ceiling orders (default: {None})

            limit {Optional[float]} -- must be included for LIMIT orders and excluded for MARKET orders (default: {None})

            client_order_id {Optional[str]} -- client-provided identifier for advanced order tracking (default: {None})

            use_awards {Optional[bool]} -- option to use Bittrex credits for the order (default: {None})

        Returns:
            Dict -- NewOrder
        """    
        return {
            Keys.MARKET_SYMBOL:self.__optionally_reversed_market_name(market),
            Keys.DIRECTION:direction,
            Keys.ORDER_TYPE:type,
            Keys.TIME_IN_FORCE:time_in_force,
            Keys.QUANTITY:quantity,
            Keys.CEILING:ceiling,
            Keys.LIMIT:limit,
            Keys.CLIENT_ORDER_ID:client_order_id,
            Keys.USE_AWARDS:use_awards,
        }

    def create_new_cancel_order_dict(
        self,
        type: CancelOrderType,
        uuid: str
    ) -> Dict:
        """order or conditional order to cancel 

        Arguments:
            type {CancelOrderType} -- type of order to cancel
            uuid {str} -- uuid of the order or conditional order to cancel

        Returns:
            Dict -- NewCancelConditionalOrder
        """
        return {
            Keys.ORDER_TYPE:type,
            Keys.ID:uuid
        }


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    def __request(
        self,
        *endpoint_args,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        method: RequestMethod = RequestMethod.GET,
        signed: bool = False,
        needed_values: Optional[Dict] = None,
        unwanted_values: Optional[Dict] = None,
        path: Optional[List] = None
    ) -> Optional[JSONData]:
        from .utils import crypto

        nonce = str(crypto.nonce)
        url = self.url_utils.url(*endpoint_args, params=params, use_nonce=False)
        headers = {'Content-Type': 'application/json'}

        if signed:
            content = ''

            if body is not None:
                body = enums.enum_free_dict(body)

                import json

                content = json.dumps(body)

            content_hash = crypto.sha512(content)
            signature = crypto.signature(
                ''.join([str(nonce), url, method.value, content_hash]),
                self.api_secret
            )

            headers = {
                'Api-Timestamp': nonce,
                'Api-Key': self.api_key,
                'Content-Type': 'application/json',
                'Api-Content-Hash': content_hash,
                'Api-Signature': signature
            }

        return self.requests.request(
            url,
            method,
            params=params,
            headers=headers,
            data=body,
            needed_values=needed_values,
            unwanted_values=unwanted_values or ['code'],
            path=path
        )

    def __optionally_reversed_market_name(self, market_name: Optional[str]) -> Optional[str]:
        return market_name if market_name is None or not self.REVERSE_MARKET_NAMES else '-'.join(market_name.split('-')[::-1])


# ---------------------------------------------------------------------------------------------------------------------------------------- #