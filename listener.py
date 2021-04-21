from pynput import keyboard
from app import click_random_legend
import json

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

def on_press(key):
            if key == keyboard.Key[ACTIVATION_BUTTON]:
                click_random_legend()

def on_release(key):
    pass

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