from graphics import *
import time

class Cell():
    def __init__(self, *, win: Window = None, x: int, y: int, width: int, height: int, has_left: bool = True, has_top: bool = True, has_right: bool = True, has_bottom: bool = True) -> None:
        self._win = win
        self.center = Point(x, y)
        self.width = width
        self.height = height
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bot = has_bottom
        self.walls = []

        self.create_lines()

    def create_lines(self):
        half_w = self.width / 2
        half_h = self.height / 2
        x = self.center.x
        y = self.center.y

        top_right = Point(x + half_w, y - half_h)
        top_left = Point(x - half_w, y - half_h)
        bot_right = Point(x + half_w, y + half_h)
        bot_left = Point(x - half_w, y + half_h)

        if self.has_top:
            self.walls.append(Line(top_left, top_right))
        if self.has_bot:
            self.walls.append(Line(bot_left, bot_right))
        if self.has_right:
            self.walls.append(Line(top_right, bot_right))
        if self.has_left:
            self.walls.append(Line(top_left, bot_left))
    
    def draw(self):
        for wall in self.walls:
            self._win.draw_line(wall, "black")
    
    def draw_path_to(self, other, undo=False):
        color = "red" if undo else "grey"
        path = Line(self.center, other.center)
        self._win.draw_line(path, color)

class Maze():
    def __init__(
            self,
            *,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size: int,
            win: Window = None
            ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win
        self.cells = None

        self._create_cells()
    
    def _create_cells(self) -> None:
        cells = []
        for i in range(self.num_rows):
            y = self.y1 + self.cell_size * i
            row = []
            for j in range(self.num_cols):
                x = self.x1 + self.cell_size * j
                row.append(Cell(win=self._win, x=x, y=y, width=self.cell_size, height=self.cell_size))
            cells.append(row)
        self.cells = cells
        self._draw_cells()
    
    def _draw_cells(self) -> None:
        if self._win == None:
            return
        for row in self.cells:
            for cell in row:
                cell.draw()
                self._animate()
    
    def _animate(self) -> None:
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.5)
