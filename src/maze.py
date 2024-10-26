from graphics import *
import time
import random

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
        self.visited = False
        self.walls: list[tuple[Line, str]] = []

        self.create_lines()
    
    def __repr__(self) -> str:
        return f"Cell: [{self.center.x},{self.center.y}] [{self.width}, {self.height}]\n  [T:{self.has_top},B:{self.has_bot},R:{self.has_right},L:{self.has_left}]"

    def create_lines(self):
        half_w = self.width / 2
        half_h = self.height / 2
        x = self.center.x
        y = self.center.y

        top_right = Point(x + half_w, y - half_h)
        top_left = Point(x - half_w, y - half_h)
        bot_right = Point(x + half_w, y + half_h)
        bot_left = Point(x - half_w, y + half_h)

        get_color = lambda should: "black" if should else "#d9d9d9"

        self.walls = [
            (Line(top_left, top_right), get_color(self.has_top)),
            (Line(bot_left, bot_right), get_color(self.has_bot)),
            (Line(top_right, bot_right), get_color(self.has_right)),
            (Line(top_left, bot_left), get_color(self.has_left))
        ]
    
    def draw(self):
        for wall, color in self.walls:
            self._win.draw_line(wall, color)
    
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
            win: Window = None,
            seed: int = None
            ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win
        self.cells: list[list[Cell]] = None

        if seed != None:
            random.seed(seed)

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
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
    
    def _is_valid_coord(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows
    
    def get_cell(self, x: int, y: int) -> Cell | None:
        if self._is_valid_coord(x, y):
            return self.cells[y][x]
        return None

    def _is_visited(self, x: int, y: int) -> bool:
        return self.get_cell(x, y).visited
    
    def _draw_cell(self, x: int, y: int, wait: float = 0.05) -> None:
        if self._is_valid_coord(x, y):
            print(f"redrawing cell {x},{y}: {self.get_cell(x,y)}")
            self.get_cell(x, y).draw()
            self._animate(wait)
    
    def _draw_cells(self) -> None:
        if self._win == None:
            return
        for row in self.cells:
            for cell in row:
                cell.draw()
                self._animate()
    
    def _animate(self, wait: float = 0.05) -> None:
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(wait)

    def _break_entrance_and_exit(self) -> None:
        start = self.get_cell(0, 0)
        start.has_top = False
        start.create_lines()
        self._draw_cell(0, 0)

        end = self.get_cell(self.num_rows-1, self.num_cols-1)
        end.has_bot = False
        end.create_lines()
        self._draw_cell(self.num_rows-1, self.num_cols-1)
    
    def _break_walls(self, x, y) -> None:
        print(f"-> breaking [{x},{y}]")
        if not self._is_valid_coord(x, y):
            print(" < can't, out of bounds")
            return
        cur: Cell = self.get_cell(x, y)
        cur.visited = True
        to_visit = list(filter(lambda c: self._is_valid_coord(*c) and not self._is_visited(*c), [(x,y+1), (x,y-1), (x-1,y), (x+1,y)]))
        print(f" --> n:{to_visit}")
        while True:
            unvisited_count = len(to_visit)
            if unvisited_count < 1:
                print(" < none left to visit")
                break
            if unvisited_count > 1:
                i = random.randint(0, unvisited_count - 1)
                print(f" >> rolled {i}")
            else:
                i = 0
            xx, yy = to_visit.pop(i)
            next: Cell = self.get_cell(xx, yy)
            if next.visited:
                print(f"  << visited while running already skip")
                continue
            print(f"  --> next > [{xx},{yy}]")
            if xx > x:
                print(" --> right")
                cur.has_right = False
                next.has_left = False
            elif xx < x:
                print(" --> left")
                cur.has_left = False
                next.has_right = False
            if yy > y:
                print(" --> down")
                cur.has_bot = False
                next.has_top = False
            elif yy < y:
                print(" --> up")
                cur.has_top = False
                next.has_bot = False
            cur.create_lines()
            next.create_lines()
            self._draw_cell(x, y)
            self._draw_cell(xx, yy)
            self._break_walls(xx, yy)
