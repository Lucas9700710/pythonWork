import pyautogui as pg
import warn
import json
import time
warn.showWarn()
time.sleep(10)
def walk(letter,step=2):
    for n in range(step):
        pg.typewrite("letter")