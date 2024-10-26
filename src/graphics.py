from tkinter import Tk, BOTH, Canvas
from constants import *

class Point():
    x = 0
    y = 0

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"P[{self.x}, {self.y}]"

class Line():
    def __init__(self, p1: Point, p2: Point, width: int = 2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.width = width
    
    def __repr__(self) -> str:
        return f"Line p1:{self.p1}, p2:{self.p2}"
    
    def draw(self, canvas: Canvas, fill_color: str = None, over_ride_width: int = None):
        if over_ride_width != None:
            width = over_ride_width
        else:
            width = self.width
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=width)


class Window():
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title = "Maze Solver"
        self._canvas = Canvas(self._root, bg=BG_COLOR, height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self._running = False
    
    def draw_line(self, line: Line, fill_color: str = None, width: int = None):
        line.draw(self._canvas, fill_color, over_ride_width=width)
        
