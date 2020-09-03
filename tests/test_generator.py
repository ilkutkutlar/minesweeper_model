import unittest
from minesweeper_model import generator


class TestGenerator(unittest.TestCase):
    def test_random_mine_coords(self):
        width = 8
        height = 5
        mine_count = 10
        actual = generator.random_mine_coords(width, height, mine_count)

        def is_coord_valid(coord):
            return (0 <= coord[0] < width) and (0 <= coord[1] < height)

        are_all_coords_valid = all(map(is_coord_valid, actual))

        self.assertTrue(are_all_coords_valid)
        self.assertEqual(len(actual), mine_count)

        # Check there are no duplicates
        self.assertEqual(len(actual), len(set(actual)))

    def test_hints_for_field(self):
        width = 8
        height = 5
        mines = [(2, 0), (4, 2), (6, 4)]

        # x: mines
        #
        # ..x.....
        # ........
        # ....x...
        # ........
        # ......x.

        actual = generator.hints_for_field(width, height, mines)
        expected = {(0, 4): 0, (1, 4): 0, (2, 4): 0, (3, 4): 0, (4, 4): 0, (5, 4): 1, (6, 4): -1, (7, 4): 1,
                    (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 1, (4, 3): 1, (5, 3): 2, (6, 3): 1, (7, 3): 1,
                    (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 1, (4, 2): -1, (5, 2): 1, (6, 2): 0, (7, 2): 0,
                    (0, 1): 0, (1, 1): 1, (2, 1): 1, (3, 1): 2, (4, 1): 1, (5, 1): 1, (6, 1): 0, (7, 1): 0,
                    (0, 0): 0, (1, 0): 1, (2, 0): -1, (3, 0): 1, (4, 0): 0, (5, 0): 0, (6, 0): 0, (7, 0): 0}
        self.assertEqual(actual, expected)

    def test_hint_for_tile(self):
        mines = [(2, 0), (4, 2), (6, 4)]
        check_mines = [(0, 0), (3, 2), (5, 3), (4, 2)]
        expected_hints = [0, 1, 2, -1]

        for mine, expected in zip(check_mines, expected_hints):
            actual = generator.hint_for_tile(mine[0], mine[1], mines)
            self.assertEqual(actual, expected)
