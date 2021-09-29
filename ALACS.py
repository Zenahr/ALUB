import pynput
from pynput import keyboard
import lib
from lib import click_readyup_button
import json
from command_runner.elevate import elevate
from time import sleep

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

SHOULD_RUN = False

def update_should_run():
    global SHOULD_RUN
    SHOULD_RUN = not SHOULD_RUN        
    print(SHOULD_RUN)

def main():
    print('MAKE SURE TO CLOSE THIS WINDOW AFTER CLOSING APEX')
    print('TO CHANGE THE ACTIVATION KEY READ THE INSTRUCTIONS FOUND IN instructions.txt')
    print('ACTIVATION KEY IS SET TO:', '>>> ', ACTIVATION_BUTTON, ' <<<')
    print('LISTENING FOR ACTIVATION KEY ...')

    def on_press(key):
                if key == keyboard.Key[ACTIVATION_BUTTON]:
                    update_should_run()

    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    while True:
        # if SHOULD_RUN:
            sleep(1)
            click_readyup_button()


if __name__ == '__main__':
    elevate(main)