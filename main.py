import time
from datetime import datetime
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser
import pyautogui as pg

keyboard = Controller()

isStarted = False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and datetime.now().strftime("%a") == i[3]:
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]) and datetime.now().strftime("%a") == i[3]:
                keyboard.press(Key.alt)
                keyboard.press('q')
                keyboard.release(Key.alt)
                keyboard.release('q')
                time.sleep(3)
                pg.click(x=674, y=340)
                isStarted = False
                break