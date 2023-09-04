import pyautogui as pag
import random, time

curr_coords = pag.position()
afk_counter = 0

while True:
    if pag.position() == curr_coords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_coords = pag.position()
    if afk_counter > 5:
        x = random.randint(0, 1919)
        # if using second screen then it'd be greater than this value
        y = random.randint(0, 1079)
        pag.moveTo(x, y, 0.5)
        curr_coords = pag.position()
    print(f"AFK counter: {afk_counter}")
    time.sleep(2)