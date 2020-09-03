import unittest
from minesweeper_model import field


class TestPlayerField(unittest.TestCase):
    def setUp(self):
        self.field1 = field.PlayerField(field.Field(4, 4))

        self.field2 = field.PlayerField(field.Field(4, 4))
        self.field2.field.mine_coords = [(0, 0), (1, 0)]
        self.field2.open_coords = [(1, 1), (0, 1)]
        self.field2.flag_coords = [(0, 0), (2, 1)]
        self.field2.hints = {(0, 0): -1, (0, 1): 2, (0, 2): 0, (0, 3): 0,
                             (1, 0): -1, (1, 1): 2, (1, 2): 0, (1, 3): 0,
                             (2, 0): 1, (2, 1): 1, (2, 2): 0, (2, 3): 0,
                             (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}

    def test_tile(self):
        actual = self.field2.tile(1, 1)
        expected = {"hint": 2, "flag": False}
        self.assertEqual(actual, expected)

        actual = self.field2.tile(0, 0)
        # Hint is None as the mine is not open
        expected = {"hint": None, "flag": True}
        self.assertEqual(actual, expected)

        actual = self.field2.tile(1, 0)
        expected = {"hint": None, "flag": False}
        self.assertEqual(actual, expected)

    def test_nine_tiles(self):
        # o: closed tile
        # [0-9]: open tile, hint
        # X: mine
        # ----------
        # o o o o
        # o o o o
        # 2 2 o o
        # X X o o

        actual = self.field2.nine_tiles(0, 1)
        # Expect to exclude tiles outside the field.
        expected = {(0, 0): {"hint": None, "flag": True},
                    (0, 2): {"hint": None, "flag": False},
                    (1, 0): {"hint": None, "flag": False},
                    (1, 1): {"hint": 2, "flag": False},
                    (1, 2): {"hint": None, "flag": False},
                    (0, 1): {"hint": 2, "flag": False}}

        self.assertEqual(actual, expected)

    def test_open_tile(self):
        self.field1.field.mine_coords = [(0, 0)]

        # Tile without mine
        self.assertTrue(self.field1.open_tile(1, 0))
        self.assertEqual(self.field1.open_coords, [(1, 0)])

        # Tile with mine
        self.assertFalse(self.field1.open_tile(0, 0))
        self.assertEqual(self.field1.open_coords, [(1, 0)])

    def test_toggle_flag(self):
        self.field1.toggle_flag(0, 1)
        self.assertEqual(self.field1.flag_coords, [(0, 1)])

        self.field1.flag_coords = [(2, 0)]
        self.field1.toggle_flag(2, 0)
        self.assertEqual(self.field1.flag_coords, [])

        self.assertRaises(ValueError, self.field1.toggle_flag, 5, 5)
