from GameInteract import message_sender as ms
import time 
import pyautogui as pag

import pandas as pd
import math


kb = ms.keyboard_INPUT()


df = pd.read_csv("codes.csv", dtype = str)
# first_column = df.iloc[:, 0]
time.sleep(5)


for a in df["code"]:
    a = (a.zfill(4))
    # print(a)

# seperation of string into vareiables

# asplit = a.split()

    asplit = list(map(str, a))
    print(asplit)
    
    
    for i in asplit:
        
        
        # pag.write(i)

        #=-=================================== it do type numbers
        
        kb.KEY_press(i)
        time.sleep(0.5)
        kb.KEY_release(i)
        print(i)

    input()
