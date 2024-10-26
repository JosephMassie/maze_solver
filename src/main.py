from graphics import *
from maze import *

def main():
    win = Window(800, 600)
    Maze(x1=50, y1=50, num_rows=10, num_cols=10, cell_size=40, win=win, seed=10)
    win.wait_for_close()

if __name__ == "__main__":
    main()
