import pynput
from pynput import keyboard
import lib
from lib import click_random_legend, click_readyup_button
import json
from command_runner.elevate import elevate

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

def main():
    def on_press(key):
                if key == keyboard.Key[ACTIVATION_BUTTON]:
                    if not json.load(open('./config.json'))['select_random_legend']:
                        click_readyup_button()
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

if __name__ == '__main__':
    elevate(main)