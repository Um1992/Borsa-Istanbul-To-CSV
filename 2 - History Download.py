from pandas_datareader import data as pdr
import os
import pandas as pd
import yfinance as yfin
yfin.pdr_override()

df = pd.read_csv('Tickers.csv').to_numpy()
if not os.path.exists("./History Data/"):
    os.makedirs("./History Data/")

for ticker in df:
    ticker = ticker[0]
    data = pdr.get_data_yahoo(ticker , start='2020-01-01', end='2022-07-29')["Close"]
    filename = "./History Data/{}.csv".format(ticker)
    data.to_csv(filename)
    print(ticker+" Done")

