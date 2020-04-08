import pandas as pd
import yfinance as yf
Date1 = "2020-02-01"
Date2 = "2020-04-08"
tickers = ["AAPL", "FB", "AMZN"]
data = yf.download(tickers, start=Date1, end=Date2)
print(type(data))
df = pd.DataFrame(data)
df2 = pd.DataFrame(df[['Close']].T)
print(df.T)