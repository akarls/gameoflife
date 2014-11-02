import Tkinter as tk
import random

world = []
canvas = None
rows = 0
cols = 0


def init_board(filename):
    global world, cols, rows
    with open(filename, "r") as f:
        cols = int(f.readline())
        rows = int(f.readline())
        for i in xrange(rows):
            world.append([False]*cols)
        a = 0
        b = 0
        for line in f.readlines():
            for chr in line:
                if chr == "*":
                    world[b][a] = True   
                elif chr == ".":
                    world[b][a] = False
                b += 1
            b = 0
            a += 1
    create_board()


def create_board():
    global window, canvas, world
    window = tk.Tk()
    canvas = tk.Canvas(window, width=cols*10, height=rows*10, bg='grey')
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    update()


def new_world():
    global world, rows, cols
    nw = []
    for x in xrange(rows):
        a = []
        for y in xrange(cols):
            neighbours = []
            if x + 1 < rows:  # bottom
                neighbours.append(world[x+1][y])
            if x - 1 >= 0:  # top
                neighbours.append(world[x-1][y])
            if y - 1 >= 0:  # left
                neighbours.append(world[x][y-1])
            if y + 1 < cols:  # right
                neighbours.append(world[x][y+1])
            if x + 1 < rows and y + 1 < cols:  # bottom right
                neighbours.append(world[x+1][y+1])
            if x - 1 >= 0 and y - 1 >= 0:  # top left
                neighbours.append(world[x-1][y-1])
            if y - 1 >= 0 and x + 1 < rows:  # bottom left
                neighbours.append(world[x+1][y-1])
            if y + 1 < cols and x - 1 >= 0:  # top right
                neighbours.append(world[x-1][y+1])

            res = len([n for n in neighbours if n])
            if res < 2 or res > 3:
                a.append(False)
            elif res == 3:
                a.append(True)
            elif res == 2:
                a.append(world[x][y])

        nw.append(a)
    world = nw


def draw_world(world):
    global rows, cols, canvas
    canvas.delete('all')
    colors = ["blue", "yellow", "red"]
    for x in xrange(rows):
        for y in xrange(cols):
            c = random.choice(colors)
            fill = c if world[x][y] else 'black'
            canvas.create_oval(x*10, y*10, x*10+10, y*10+10, fill=fill)


def update():
    global world, window
    draw_world(world)
    new_world()
    window.after(100, update)


init_board("initialSetup1.txt")

window.mainloop()
