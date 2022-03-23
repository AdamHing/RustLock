import win32com.client as client
import time


wsh = client.Dispatch('WScript.Shell')
wsh.AppActivate("RustClient.exe")
time.sleep(4)
wsh.SendKeys('u are gay')
