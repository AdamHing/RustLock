import pandas as pd
import math

df = pd.read_csv("codes.csv", dtype = str)
# first_column = df.iloc[:, 0]



for a in df["code"]:
    a = int(a.zfill(4))
    print(a)
    digits = int(math.log10(a))+1
    if digits < 4:
            
        print(a)
        print(type(a))
        print('a')

