from graphics import *
from maze import *

def main():
    w_width = 800
    w_height = 600
    win = Window(w_width, w_height)

    gap = 10
    m_width = w_width - gap * 2
    m_height = w_height - gap * 2
    cell_size = 20
    cols = m_width // cell_size
    rows = m_height // cell_size
    x = gap + cell_size / 2
    y = gap + cell_size / 2
    Maze(x1=x, y1=y, num_rows=rows, num_cols=cols, cell_size=cell_size, win=win).solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
