# 3d-volatility-surface

What is a 3D Volatility Surface?
The 3D volatility surface is a three-dimensional plot that displays the implied volatilities of a stock's options listed across different strike prices and expirations.

This repository extracts options data from Yahoo Finance, performs minimal data manipulation, and constructs a 3D volatility surface from it. The tool is free to use, utilizing data from Yahoo Finance, and its output requires less than 100 KB of storage space.

To use this script, a chat box will prompt the user to enter a stock ticker. Then, the user will be asked to choose from a dropdown menu to select the options type (puts vs. calls) and whether the options data should be presented with a log scale.

Below is a sample result of the AAPL 3D volatility surface:

You can zoom in to view the 3D surface or pivot the chart to view the horizontal/vertical implied volatility profile of the ticker's options.

