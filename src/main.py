from graphics import *
from maze import *

def main():
    w_width = 1050
    w_height = 1050
    gap = 25
    cell_size = 100

    win = Window(w_width, w_height)

    m_width = w_width - gap * 2
    m_height = w_height - gap * 2
    cols = m_width // cell_size
    rows = m_height // cell_size
    x = gap + cell_size / 2
    y = gap + cell_size / 2

    print(f"creating a maze with {rows} rows and {cols} columns\nwith a total of {rows * cols} cells\n\n")

    Maze(x1=x, y1=y, num_rows=rows, num_cols=cols, cell_size=cell_size, win=win).solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
