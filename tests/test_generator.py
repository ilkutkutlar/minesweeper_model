import unittest
from minesweeper_model.generator import Generator


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.width = 8
        self.height = 5
        self.mines = [(2, 0), (4, 2), (6, 4)]

        # X: mines
        #
        # ......X.
        # ........
        # ....X...
        # ........
        # ..X.....

    def test_hints_for_field(self):
        actual = Generator.hints_for_field(self.width, self.height, self.mines)
        expected = {
                    (0, 4): 0, (1, 4): 0, (2, 4): 0, (3, 4): 0, (4, 4): 0, (5, 4): 1, (6, 4): -1, (7, 4): 1,
                    (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 1, (4, 3): 1, (5, 3): 2, (6, 3): 1, (7, 3): 1,
                    (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 1, (4, 2): -1, (5, 2): 1, (6, 2): 0, (7, 2): 0,
                    (0, 1): 0, (1, 1): 1, (2, 1): 1, (3, 1): 2, (4, 1): 1, (5, 1): 1, (6, 1): 0, (7, 1): 0,
                    (0, 0): 0, (1, 0): 1, (2, 0): -1, (3, 0): 1, (4, 0): 0, (5, 0): 0, (6, 0): 0, (7, 0): 0
                }
        self.assertEqual(actual, expected)

    def test_hint_for_tile(self):
        check_mines = [(0, 0), (3, 2), (5, 3), (4, 2)]
        expected_hints = [0, 1, 2, -1]

        for mine, expected in zip(check_mines, expected_hints):
            actual = Generator.hint_for_tile(mine[0], mine[1],
                                             self.width, self.height,
                                             self.mines)
            self.assertEqual(actual, expected)
