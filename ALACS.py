from pynput import keyboard
from lib import click_random_legend
import json

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

def on_press(key):
            if key == keyboard.Key[ACTIVATION_BUTTON]:
                click_random_legend()

def on_release(key):
    pass

print('BOOTING UP ALACS ...')
print('BOOTED UP ALACS')
print('LISTENING FOR ACTIVATION KEY ...')
print('MAKE SURE TO CLOSE THIS WINDOW AFTER CLOSING APEX')
print('TO CHANGE THE ACTIVATION KEY READ THE INSTRUCTIONS FOUND IN config.json')
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()