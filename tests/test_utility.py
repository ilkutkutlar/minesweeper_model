import unittest
from minesweeper_model import utility


class TestUtility(unittest.TestCase):
    def test_surrounding_tiles(self):
        actual = utility.surrounding_tiles(4, 2)
        expected = [(3, 3), (4, 3), (5, 3),
                    (3, 2), (5, 2),
                    (3, 1), (4, 1), (5, 1)]
        self.assertCountEqual(actual, expected)

    def test_surrounding_tiles_remove_outside_tiles(self):
        actual = utility.surrounding_tiles(0, 1, True)
        expected = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
        self.assertCountEqual(actual, expected)

    def test_str_input_to_mine_coords(self):
        str_field = """..x...x
.......
....x..
......x
x......"""

        x, y, mines = utility.str_input_to_mine_coords(str_field)
        expected_mines = {(2, 0), (6, 0), (4, 2), (6, 3), (0, 4)}

        self.assertEqual(x, 7)
        self.assertEqual(y, 5)
        self.assertEqual(set(mines), expected_mines)
