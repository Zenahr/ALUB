import pynput
from pynput import keyboard
import lib
from lib import click_random_legend, click_main_legends
import json

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

def on_press(key):
            if key == keyboard.Key[ACTIVATION_BUTTON]:
                if json.load(open('./config.json'))['1st_main_legend']:
                    click_main_legends()
                else:
                    click_random_legend()

def on_release(key):
    pass

print('BOOTING UP ALACS ...')
print('BOOTED UP ALACS')
print('MAKE SURE TO CLOSE THIS WINDOW AFTER CLOSING APEX')
print('TO CHANGE THE ACTIVATION KEY READ THE INSTRUCTIONS FOUND IN instructions.txt')
print('ACTIVATION KEY IS SET TO:', '>>> ', ACTIVATION_BUTTON, ' <<<')
print('LISTENING FOR ACTIVATION KEY ...')
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()