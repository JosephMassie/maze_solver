import unittest
import sys

sys.path.append('./src')

from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(x1=0, y1=0, num_rows=num_rows, num_cols=num_cols, cell_size=10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()
