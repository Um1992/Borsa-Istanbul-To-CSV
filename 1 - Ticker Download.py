import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.kap.org.tr/en/Pazarlar"
page = requests.get(URL).text


pagebs = BeautifulSoup(page, "lxml")

tickers = []
for i in pagebs.find("div", attrs={"class":"column-type7 wmargin"}).find_all("div", attrs={"class" : "comp-cell _02 vtable"}):
 ticker = i.text.replace('\n', ' ').strip()
 tickers.append(ticker+".IS")


tl = pd.DataFrame(tickers)
tl.to_csv("Tickers.csv", index=False, header=False)