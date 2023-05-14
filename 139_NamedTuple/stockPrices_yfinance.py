import yfinance as yf
from collections import namedtuple

StockPrice = namedtuple('StockPrice', ['symbol', 'date', 'open', 'close'])

def get_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    open_price = hist["Open"].values[0]
    close_price = hist["Close"].values[0]
    date = hist.index.strftime('%Y-%m-%d')[0]
    return StockPrice(symbol, date, open_price, close_price)
    
# Usage example
symbol = 'AAPL'
stock_price = get_stock_price(symbol)
print(stock_price.symbol)  # output: 'AAPL'
print(stock_price.date)    # output: '2022-05-13'
print(stock_price.open)    # output: 127.82
print(stock_price.close)   # output: 128.10
