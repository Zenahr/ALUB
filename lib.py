import random
import autopy
import pyautogui
import time

# 1920::1080
legends = [
(1141, 366), # BLOODHOUND 0
(1277, 360), # GIBRALTAR 1
(1390, 363), # LIFELINE 2
(1496, 359), # PATHFINDER 3
(1630, 358), # WRAITH 4
(1109, 483), # BANGALORE 5
(1231, 475), # CAUSTIC 6
(1353, 484), # MIRAGE 7
(1464, 482), # OCTANE 8
(1588, 492), # WATTSON 9
(1702, 492), # CRYPTO 10
(1183, 612), # REVENANT 11
(1306, 613), # LOBA 12
(1424, 611), # RAMPART 13
(1549, 611), # HORIZON 14
(1670, 612)  # FUSE 15
]

def get_legend_name_by_index(index):
    if   index == 0:
        return 'BLOODHOUND'
    elif index == 1:
        return 'GIBRALTAR'
    elif index == 2:
        return 'LIFELINE'
    elif index == 3:
        return 'PATHFINDER'
    elif index == 4:
        return 'WRAITH'
    elif index == 5:
        return 'BANGALORE'
    elif index == 6:
        return 'CAUSTIC'
    elif index == 7:
        return 'MIRAGE'
    elif index == 8:
        return 'OCTANE'
    elif index == 9:
        return 'WATTSON'
    elif index == 10:
        return 'CRYPTO'
    elif index == 11:
        return 'REVENANT'
    elif index == 12:
        return 'LOBA'
    elif index == 13:
        return 'RAMPART'
    elif index == 14:
        return 'HORIZON'
    else:
        return 'FUSE'

def get_index_by_legend_name(name):
    if   name == 'BLOODHOUND': 
        return 0
    elif name == 'GIBRALTAR': 
        return 1
    elif name == 'LIFELINE': 
        return 2
    elif name == 'PATHFINDER': 
        return 3
    elif name == 'WRAITH': 
        return 4
    elif name == 'BANGALORE': 
        return 5
    elif name == 'CAUSTIC': 
        return 6
    elif name == 'MIRAGE': 
        return 7
    elif name == 'OCTANE': 
        return 8
    elif name == 'WATTSON': 
        return 9
    elif name == 'CRYPTO': 
        return 10
    elif name == 'REVENANT': 
        return 11
    elif name == 'LOBA': 
        return 12
    elif name == 'RAMPART': 
        return 13
    elif name == 'HORIZON': 
        return 14
    elif name == 'FUSE':
        return 15

def get_position():
    print(
    pyautogui.position()
    )

def click_random_legend():
    random_index = random.randint(0, len(legends)-1)
    autopy.mouse.move(*legends[random_index])
    print('selected legend:', get_legend_name_by_index(random_index))
    time.sleep(.2)
    autopy.mouse.click()