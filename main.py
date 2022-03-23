from GameInteract import message_sender as ms
import time 
import pandas as pd
import keyboard

kb = ms.keyboard_INPUT()
df = pd.read_csv("codes.csv", dtype = str)
time.sleep(5)


for a in df["code"]:
    a = (a.zfill(4))


    asplit = list(map(str, a))
    print(asplit)
    
    
    while True:
        if keyboard.read_key() == "p":
            print("You pressed p")
            break
    for i in asplit:
#=-=================================== it do type numbers  
        kb.KEY_press(i)
        time.sleep(0.5)
        kb.KEY_release(i)
        print(i)





