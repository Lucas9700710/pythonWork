import pyautogui as pg
import warn
import json
import time
warn.showWarn()
time.sleep(5)
def walk(letter,step=10):
    for n in range(step):
        pg.typewrite(letter)
walk("w",5)
