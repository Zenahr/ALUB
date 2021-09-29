import random
import autopy
import pyautogui
import time
import json
from threading import Timer
import cv2
import pytesseract

def click_readyup_button():
    print('CHECKING...')
    if should_click():
        try:
            autopy.mouse.move(*(230, 928))
            time.sleep(.2)
            autopy.mouse.click()
        except TypeError:
            print('INTERNAL ERROR OCCURED. CONTACT DEVELOPER.')

def get_position():
    print(
    pyautogui.position()
    )

def should_click():
    box = ((140, 950), (170, 42))
    screenshot = autopy.bitmap.capture_screen(box)
    screenshot.save('screenshot.png')
    img = cv2.imread('screenshot.png')
    threshold = 90
    gray      = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh    = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)[1]
    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)
    scanned_text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    try:
        print(scanned_text)
        if 'READY' in scanned_text:
            print('read READY in screenshot')
            return True
        elif 'CANCEL' in scanned_text:
            print('read CANCEL in screenshot')
            return True
        else:
            print('read nothing in screenshot')
            return False
    except AttributeError:
        raise Exception(f'OCR MODULE: COULD NOT RETRIEVE TEXT')

if __name__ == '__main__':
    print(
    should_click()
    )