from tkinter import *
from tkinter import messagebox as tkMessageBox
from collections import deque
import random
import platform
from datetime import datetime

GRID_SIZE_X = 16
GRID_SIZE_Y = 16

STATE_DEFAULT = 0
STATE_CLICKED = 1
STATE_FLAGGED = 2

BTN_LEFT_CLICK = "<Button-1>"
BTN_RIGHT_CLICK = "<Button-2>" if platform.system() == 'Darwin' else "<Button-3>"

main_window = None

class MinesweeperGame:

    def __init__(self, tk):

        # import images
        self.images = {
            "plain": PhotoImage(file = "images/tile_plain.gif"),
            "clicked": PhotoImage(file = "images/tile_clicked.gif"),
            "mine": PhotoImage(file = "images/tile_mine.gif"),
            "flag": PhotoImage(file = "images/tile_flag.gif"),
            "wrong": PhotoImage(file = "images/tile_wrong.gif"),
            "numbers": []
        }
        for i in range(1, 9):
            self.images["numbers"].append(PhotoImage(file = "images/tile_"+str(i)+".gif"))

        # set up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # set up labels/UI
        self.labels = {
            "time": Label(self.frame, text = "00:00:00"),
            "mines": Label(self.frame, text = "Mines: 0"),
            "flags": Label(self.frame, text = "Flags: 0")
        }
        self.labels["time"].grid(row = 0, column = 0, columnspan = GRID_SIZE_Y) # top full width
        self.labels["mines"].grid(row = GRID_SIZE_X+1, column = 0, columnspan = int(GRID_SIZE_Y/2)) # bottom left
        self.labels["flags"].grid(row = GRID_SIZE_X+1, column = int(GRID_SIZE_Y/2)-1, columnspan = int(GRID_SIZE_Y/2)) # bottom right

        self.restart() # start game
        self.update_timer() # init timer

    def setup(self):
        # create flag and clicked tile variables
        self.flag_count = 0
        self.correct_flag_count = 0
        self.clicked_count = 0
        self.start_time = None

        # create buttons
        self.tiles = dict({})
        self.mines = 0
        for x in range(0, GRID_SIZE_X):
            for y in range(0, GRID_SIZE_Y):
                if y == 0:
                    self.tiles[x] = {}

                id = str(x) + "_" + str(y)
                is_mine = False

                # tile image changeable for debug reasons:
                gfx = self.images["plain"]

                # currently random amount of mines
                if random.uniform(0.0, 1.0) < 0.1:
                    is_mine = True
                    self.mines += 1

                tile = {
                    "id": id,
                    "is_mine": is_mine,
                    "state": STATE_DEFAULT,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "button": Button(self.frame, image = gfx),
                    "mines": 0 # calculated after grid is built
                }

                tile["button"].bind(BTN_LEFT_CLICK, self.on_click_wrapper(x, y))
                tile["button"].bind(BTN_RIGHT_CLICK, self.on_right_click_wrapper(x, y))
                tile["button"].grid( row = x+1, column = y ) # offset by 1 row for timer

                self.tiles[x][y] = tile

        # loop again to find nearby mines and display number on tile
        for x in range(0, GRID_SIZE_X):
            for y in range(0, GRID_SIZE_Y):
                mc = 0
                for n in self.get_neighbors(x, y):
                    mc += 1 if n["is_mine"] else 0
                self.tiles[x][y]["mines"] = mc

    def restart(self):
        self.setup()
        self.refresh_labels()

    def refresh_labels(self):
        self.labels["flags"].config(text = "Flags: "+str(self.flag_count))
        self.labels["mines"].config(text = "Mines: "+str(self.mines))

    def game_over(self, won):
        for x in range(0, GRID_SIZE_X):
            for y in range(0, GRID_SIZE_Y):
                if self.tiles[x][y]["is_mine"] == False and self.tiles[x][y]["state"] == STATE_FLAGGED:
                    self.tiles[x][y]["button"].config(image = self.images["wrong"])
                if self.tiles[x][y]["is_mine"] == True and self.tiles[x][y]["state"] != STATE_FLAGGED:
                    self.tiles[x][y]["button"].config(image = self.images["mine"])

        self.tk.update()

        msg = "You Win! Play again?" if won else "You Lose! Play again?"
        res = tkMessageBox.askyesno("Game Over", msg)
        if res:
            self.restart()
        else:
            self.tk.quit()

    def update_timer(self):
        ts = "00:00:00"
        if self.start_time != None:
            delta = datetime.now() - self.start_time
            ts = str(delta).split('.')[0] # drop ms
            if delta.total_seconds() < 36000:
                ts = "0" + ts # zero-pad
        self.labels["time"].config(text = ts)
        self.frame.after(100, self.update_timer)

    def get_neighbors(self, x, y):
        neighbors = []
        coords = [
            {"x": x-1,  "y": y-1},  #top right
            {"x": x-1,  "y": y},    #top middle
            {"x": x-1,  "y": y+1},  #top left
            {"x": x,    "y": y-1},  #left
            {"x": x,    "y": y+1},  #right
            {"x": x+1,  "y": y-1},  #bottom right
            {"x": x+1,  "y": y},    #bottom middle
            {"x": x+1,  "y": y+1},  #bottom left
        ]
        for n in coords:
            try:
                neighbors.append(self.tiles[n["x"]][n["y"]])
            except KeyError:
                pass
        return neighbors

    def on_click_wrapper(self, x, y):
        return lambda Button: self.on_click(self.tiles[x][y])

    def on_right_click_wrapper(self, x, y):
        return lambda Button: self.on_right_click(self.tiles[x][y])

    def on_click(self, tile):
        if self.start_time == None:
            self.start_time = datetime.now()

        if tile["is_mine"] == True:
            # end game
            self.game_over(False)
            return

        # change image
        if tile["mines"] == 0:
            tile["button"].config(image = self.images["clicked"])
            self.clear_surrounding_tiles(tile["id"])
        else:
            tile["button"].config(image = self.images["numbers"][tile["mines"]-1])
        # if not already set as clicked, change state and count
        if tile["state"] != STATE_CLICKED:
            tile["state"] = STATE_CLICKED
            self.clicked_count += 1
        if self.clicked_count == (GRID_SIZE_X * GRID_SIZE_Y) - self.mines:
            self.game_over(True)

    def on_right_click(self, tile):
        if self.start_time == None:
            self.start_time = datetime.now()

        # if not clicked
        if tile["state"] == STATE_DEFAULT:
            tile["button"].config(image = self.images["flag"])
            tile["state"] = STATE_FLAGGED
            tile["button"].unbind(BTN_LEFT_CLICK)
            # if a mine
            if tile["is_mine"] == True:
                self.correct_flag_count += 1
            self.flag_count += 1
            self.refresh_labels()
        # if flagged, unflag
        elif tile["state"] == 2:
            tile["button"].config(image = self.images["plain"])
            tile["state"] = 0
            tile["button"].bind(BTN_LEFT_CLICK, self.on_click_wrapper(tile["coords"]["x"], tile["coords"]["y"]))
            # if a mine
            if tile["is_mine"] == True:
                self.correct_flag_count -= 1
            self.flag_count -= 1
            self.refresh_labels()

    def clear_surrounding_tiles(self, id):
        queue = deque([id])

        while len(queue) != 0:
            key = queue.popleft()
            parts = key.split("_")
            x = int(parts[0])
            y = int(parts[1])

            for tile in self.get_neighbors(x, y):
                self.clear_tile(tile, queue)

    def clear_tile(self, tile, queue):
        if tile["state"] != STATE_DEFAULT:
            return

        if tile["mines"] == 0:
            tile["button"].config(image = self.images["clicked"])
            queue.append(tile["id"])
        else:
            tile["button"].config(image = self.images["numbers"][tile["mines"]-1])

        tile["state"] = STATE_CLICKED
        self.clicked_count += 1

def main():
    # create Tk instance
    window = Tk()
    # set program title
    window.title("Minesweeper")
    # create game instance
    minesweeper = MinesweeperGame(window)
    # run event loop
    window.mainloop()

if __name__ == "__main__":
    main()
