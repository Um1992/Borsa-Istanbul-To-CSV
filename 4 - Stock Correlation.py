import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

bigData = pd.read_csv("MergedData.csv")
hisseList = []

while True:
    try:
        sayi=int((input("Kaç tane hissenin kolerasyonuna bakacaksınız? \n")))
        break
    except ValueError:
        print("Sadece Sayı Girin")

for i in range(sayi):

    while True:
        try:
            ticker = input(str(i+1)+" numaralı hissenin kodunu giriniz. \n").upper()
            hisseList.append(ticker)
            break
        except:
            print("Lütfen geçerli hisse kodu giriniz.")

secilenler = bigData[hisseList]
secilenler = secilenler.dropna().corr()
print(secilenler)

hP = sns.heatmap(secilenler, linewidths=0.5, cmap="RdBu")
plt.show()