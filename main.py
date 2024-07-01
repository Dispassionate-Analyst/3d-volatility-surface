


# __main__.py

from data_fetching import fetch_expiry_dates
from calculations import build_volatility_surface
from plotting import plot_volatility_surface
from user_input import get_user_input

def main():
    """Main function to execute the volatility surface plot."""
    symbol, option_type, use_log = get_user_input()

    expiry_dates = fetch_expiry_dates(symbol)

    X, Y, Z, expiry_dates = build_volatility_surface(symbol, expiry_dates, option_type, use_log)
    plot_volatility_surface(X, Y, Z, expiry_dates, symbol)

if __name__ == "__main__":
    main()