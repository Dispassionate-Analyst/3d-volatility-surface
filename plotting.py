

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_volatility_surface(X, Y, Z, expiry_dates, symbol):
    """Plots the volatility surface for the given data."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(X, Y, Z, cmap='viridis')
    ax.set_xlabel('Expiry Dates')
    ax.set_ylabel('Strike Prices')
    ax.set_zlabel('Implied Volatility')
    ax.set_title(f'Volatility Surface for {symbol}')  # Set the chart title to the ticker symbol

    # Show only every 3rd expiry date on x-axis for cleaner presentation
    ax.set_xticks(np.arange(0, len(expiry_dates), 3))
    ax.set_xticklabels(expiry_dates[::3])

    plt.show()

