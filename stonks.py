import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
plt.style.use('ggplot')

today = date.today()
fiveYearsAgo = today - timedelta(days=(365 * 5))
tickerSymbols = []
profitArray = []

numStocks = input("How many stocks would you like to see?: ")

for i in range(int(numStocks)):
    # Prompt user for the ticker symbol
    tickerSymbol = input("Please enter the ticker symbol for the next stock: ")
    # Store it in the symbols array for the chart
    tickerSymbols.insert(0, tickerSymbol)
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=fiveYearsAgo, end=today)
    # Get the closing price
    s = tickerDf['Close']
    # Get the difference of the closing price between five years ago and now
    dates = pd.date_range(fiveYearsAgo, periods=1825)
    diff = s[dates[1824]] - s[dates[0]]
    # Store it in the profit array for the chart
    profitArray.insert(0, diff)

# Prepare labels for the x axis
x_pos = [i for i, _ in enumerate(tickerSymbols)]

plt.bar(x_pos, profitArray, color='green')
plt.xlabel("Ticker Symbol")
plt.ylabel("Profit (USD)")
plt.title("Price performance in the last 5 years")

plt.xticks(x_pos, tickerSymbols)

plt.show()
