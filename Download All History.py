from pandas_datareader.data import DataReader
import pandas as pd

df = pd.read_csv('Tickers.csv').to_numpy()

for ticker in df:
    data = DataReader(ticker, 'yahoo', start='2020-01-01', end='2022-07-29')["Close"]
    filename = "History Data/{}.csv".format(ticker)
    data.to_csv(filename)
    print(ticker+" Done")