

import numpy as np

def calculate_implied_volatility(option_chain, option_type, use_log):
    """Calculates the implied volatility from the option chain."""
    implied_volatilities = option_chain[0 if option_type == 'calls' else 1]['impliedVolatility'].to_numpy()
    if use_log:
        return np.log(implied_volatilities)  # Log-transform the implied volatilities
    else:
        return implied_volatilities

def smooth_implied_volatility(implied_volatilities):
    """Smooths strikes that return 0% IV from yahoo finance."""
    smoothed_iv = np.copy(implied_volatilities)
    zero_indices = np.where(smoothed_iv == 0)[0]

    for idx in zero_indices:
        left_idx = idx - 1
        right_idx = idx + 1

        while left_idx in zero_indices:
            left_idx -= 1

        while right_idx in zero_indices:
            right_idx += 1

        if left_idx >= 0 and right_idx < len(implied_volatilities):
            smoothed_iv[idx] = (implied_volatilities[left_idx] + implied_volatilities[right_idx]) / 2

    return smoothed_iv

def build_volatility_surface(symbol, expiry_dates, option_type, use_log):
    """Builds the volatility surface for the given symbol and option type."""
    from data_fetching import fetch_option_chain  # Local import to avoid circular dependencies

    all_strikes = []
    all_implied_volatilities = []
    expiry_indices = []

    for i, expiry_date in enumerate(expiry_dates):
        option_chain = fetch_option_chain(symbol, expiry_date)
        implied_volatilities = calculate_implied_volatility(option_chain, option_type, use_log)

        if len(implied_volatilities) == 0:
            print(f"No {option_type} data found in option chain")
            continue

        smoothed_iv = smooth_implied_volatility(implied_volatilities)

        strikes = option_chain[0 if option_type == 'calls' else 1]['strike'].to_numpy()

        all_strikes.extend(strikes)
        all_implied_volatilities.extend(smoothed_iv)
        expiry_indices.extend([i] * len(strikes))

    X = np.array(expiry_indices)
    Y = np.array(all_strikes)
    Z = np.array(all_implied_volatilities)

    return X, Y, Z, expiry_dates
