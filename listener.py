from pynput import keyboard
import pyautogui
from app import click_random_legend

def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
            # key.char))
            if key == keyboard.Key.home:
                print('selecting random legend')
                click_random_legend()
    except AttributeError:
        # print('special key {0} pressed'.format(
        #     key))
        pass

def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return True
        # return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()