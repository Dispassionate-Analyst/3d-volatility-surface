

import yfinance as yf

def fetch_expiry_dates(symbol):
    """Fetches the expiry dates for the given symbol."""
    expiry_dates = yf.Ticker(symbol).options
    return expiry_dates

def fetch_option_chain(symbol, expiry_date):
    """Fetches the option chain for the given symbol and expiry date."""
    option_chain = yf.Ticker(symbol).option_chain(expiry_date)
    return option_chain

