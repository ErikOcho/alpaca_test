# main.py

import alpaca_trade_api as tradeapi
from credentials import KEY, SECRET, ENDPOINT
from alpaca_trade_api.entity import Account
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import pandas as pd

def connect_to_api() -> REST:
    api = REST(
        KEY,
        SECRET,
        ENDPOINT
    )
    return api


def get_account(api: REST) -> Account:
    account: Account = api.get_account()
    return account


def get_barset(api: REST, name: str, start_time: str, end_time: str = None):
    asset = api.get_bars(name, timeframe=TimeFrame(1, TimeFrameUnit.Day), start=start_time, end=end_time, adjustment='raw')
    return asset


def test():
    api = connect_to_api()
    account: Account = get_account(api)
    apple_prices = get_barset(api, 'AAPL', '2019-01-01','2023-01-05')['AAPL']
    print(apple_prices[0])


def main():
    api = connect_to_api()
    account: Account = get_account(api)
    print(f"Your equity is {account.equity}.")
    pd.DataFrame(get_barset(api, 'AAPL', '2019-01-01','2023-01-05'))

    test()


if __name__ == '__main__':
    main()