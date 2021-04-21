import random
import autopy
import pyautogui
import time

# 1920::1080
legends = [
(1141, 366), # BLOODHOUND
(1277, 360), # GIBRALTAR
(1390, 363), # LIFELINE
(1496, 359), # PATHFINDER
(1630, 358), # WRAITH
(1109, 483), # BANGALORE
(1231, 475), # CAUSTIC
(1353, 484), # MIRAGE
(1464, 482), # OCTANE
(1588, 492), # WATTSON
(1702, 492), # CRYPTO
(1183, 612), # REVENANT
(1306, 613), # LOBA
(1424, 611), # RAMPART
(1549, 611), # HORIZON
(1670, 612)  # FUSE
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