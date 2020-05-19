import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # Create a dictionary 
    vol_dic = dict()
    vol = prices.pivot(index='date', columns='ticker', values='price')
    
    # Iterate through each ticker
    for i in vol.columns:
        std = vol[i].std()
        vol_dic[i] = std
    
    # Return the max standard deviation ticker
    max_ticker = max(vol_dic, key=vol_dic.get)
    return max_ticker


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
