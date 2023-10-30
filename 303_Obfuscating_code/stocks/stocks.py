import datetime as dt
import yfinance as yf

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

df = yf.download("AAPL", start=start, end=end)

print(df)
