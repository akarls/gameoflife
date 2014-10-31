import Tkinter as tk

def init_board(filename):
    global world, cols, rows
    with open(filename, "r") as f:
        cols = int(f.readline())
        rows = int(f.readline())
        world = []
        for i in range(rows):
            world.append([False]*cols)
        a=0
        b=0
        for line in f.readlines():
            for chr in line:
                if chr == "*":
                    world[b][a] = True   
                elif chr == ".":
                    world[b][a] = False
                b+=1
            b=0
            a+=1

    create_board()

def create_board():
    global window, canvas, world
    window = tk.Tk()
    canvas = tk.Canvas(window, width=cols*10, height=rows*10, bg='black')
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    update()

def update():
    global window, canvas, world
    l=0
    o=0
    for line in range(1,rows-1):
        for obj in range(1,cols-1):
            if not world[l][o]:
		if ne(l,o) == 3:
			on(l,o)
			break
	    if world[l][o]:
		if ne(l,o) >= 4:
			off(l,o)
			break
		if ne(l,o) < 2:
			off(l,o)
			break
		if ne(l,o) == 2 or 3:
			on(l,o)
			break
            o+=1
        o=0
        l+=1

    window.after(100, update)

def ne(r,c):
    i = 0
    if world[r][c+1]:
        i+=1
    if world[r][c-1]:
        i+=1
    if world[r-1][c]:
        i+=1
    if world[r+1][c]:
        i+=1 
    if world[r-1][c-1]:
        i+=1
    if world[r-1][c+1]:
        i+=1
    if world[r+1][c-1]: 
        i+=1
    if world[r+1][c+1]:
        i+=1
    return int(i)
    
def on(row, col):
    global canvas
    world[row][col] = True
    row *= 10
    col *= 10
    canvas.create_rectangle(row, col, row+10, col+10, fill='yellow')

def off(row, col):
    global canvas
    world[row][col] = False
    row *= 10
    col *= 10
    canvas.create_rectangle(row, col, row+10, col+10, fill='black')

init_board("initialSetup1.txt")

window.mainloop()
