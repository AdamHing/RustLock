from GameInteract import message_sender as ms
import time 
kb = ms.keyboard_INPUT()

time.sleep(5)
kb.KEY_press("w")
time.sleep(4)
kb.KEY_release("w")
kb.KEY_press("s")
time.sleep(2)
kb.KEY_release("s")

kb.KEY_press("d")
time.sleep(2)
kb.KEY_release("d")