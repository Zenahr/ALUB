import pynput
from pynput import keyboard
import lib
from lib import click_readyup_button
import json
from command_runner.elevate import elevate
from time import sleep
from threading import Thread
import keyboard

ACTIVATION_BUTTON = json.load(open('./config.json'))['key']

SHOULD_RUN = False

def update_should_run():
    global SHOULD_RUN
    SHOULD_RUN = not SHOULD_RUN        
    print(SHOULD_RUN)

thread = Thread(target=click_readyup_button, daemon=True)

def main():
    print('MAKE SURE TO CLOSE THIS WINDOW AFTER CLOSING APEX')
    print('TO CHANGE THE ACTIVATION KEY READ THE INSTRUCTIONS FOUND IN instructions.txt')
    print('ACTIVATION KEY IS SET TO:', '>>> ', ACTIVATION_BUTTON, ' <<<')
    print('LISTENING FOR ACTIVATION KEY ...')

    while True:
        if SHOULD_RUN:
            sleep(1)
            if not thread.is_alive():
                thread.start()
        elif not SHOULD_RUN:
            if thread.is_alive():
                thread.join()
        if keyboard.is_pressed('b') == True:
            update_should_run()


if __name__ == '__main__':
    elevate(main)