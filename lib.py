import random
import autopy
import pyautogui
import time
import json
from threading import Timer

def click_readyup_button():
    print('RUNNING AUTO-READY')
    try:
        autopy.mouse.move(*(230, 928))
        time.sleep(.2)
        autopy.mouse.click()
    except TypeError:
        print('INTERNAL ERROR OCCURED. CONTACT DEVELOPER.')
        click_random_legend()

def get_position():
    print(
    pyautogui.position()
    )