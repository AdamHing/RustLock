import pandas as pd
import math

df = pd.read_csv("codes.csv", dtype = str)
# first_column = df.iloc[:, 0]



for a in df["code"]:
    a = (a.zfill(4))
    print(a)

# seperation of string into vareiables

# asplit = a.split()

    asplit = list(map(str, a))
    print(asplit)

