import glob, os
import pandas as pd

csvList = glob.glob(os.path.join("History Data", "*.csv"))
merged = pd.DataFrame()
for i in csvList:
    print(i.format(i)[13:][:-7])
    ticker = pd.read_csv(i)
    ticker = ticker.rename(columns={"Close":"{}".format(i)[13:][:-7]})
    ticker.set_index("Date")
    merged = merged.join(ticker.set_index(["Date"]),how="outer")

    merged.to_csv("MergedData.csv")