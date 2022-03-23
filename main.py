from GameInteract import message_sender as ms
import time 
kb = ms.keyboard_INPUT()

time.sleep(5)
kb.KEY_press("w")
kb.KEY_release("w")
kb.KEY_press("h")
kb.KEY_release("h")
kb.KEY_press("i")
kb.KEY_release("i")

