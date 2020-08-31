import unittest
from minesweeper_model.field import *

class TestField(unittest.TestCase):

    def test_hint_for_tile(self):
        width = 8
        height = 5
        mines = [(2, 0), (4, 2), (6, 4)]
        
        # X: mines
        # -: test positions
        #
        # ......X.
        # .....-..
        # ...-X...
        # ........
        # -.X.....

        self.assertEqual(hint_for_tile(0, 0, width, height, mines), 0)
        self.assertEqual(hint_for_tile(3, 2, width, height, mines), 1)
        self.assertEqual(hint_for_tile(5, 3, width, height, mines), 2)
