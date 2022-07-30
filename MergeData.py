import glob, os
import pandas as pd
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("History Data", "*.csv"))),axis=1)
df.to_csv("AllMerged.csv")