from collections import namedtuple

StockPrice = namedtuple('StockPrice', ['symbol', 'date', 'open', 'close'])

def parse_stock_price(line):
    fields = line.strip().split(',')
    symbol, date, open_price, close_price = fields
    return StockPrice(symbol, date, float(open_price), float(close_price))
    
# Usage example
line = 'AAPL,2022-05-13,127.82,128.10'
stock_price = parse_stock_price(line)
print(stock_price.symbol)  # output: 'AAPL'
print(stock_price.date)    # output: '2022-05-13'
print(stock_price.open)    # output: 127.82
print(stock_price.close)   # output: 128.10
