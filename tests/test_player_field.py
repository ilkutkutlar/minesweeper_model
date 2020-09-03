import unittest
from minesweeper_model import field


class TestPlayerField(unittest.TestCase):
    def setUp(self):
        self.player_field = field.PlayerField(field.Field(4, 4))

    def test_open_tile(self):
        self.player_field.field.mine_coords = [(0, 0)]

        self.assertTrue(self.player_field.open_tile(1, 0))
        self.assertEqual(self.player_field.open_coords, [(1, 0)])

        self.assertFalse(self.player_field.open_tile(0, 0))
        self.assertEqual(self.player_field.open_coords, [(1, 0)])

    def test_toggle_flag(self):
        self.player_field.toggle_flag(0, 1)
        self.assertEqual(self.player_field.flag_coords, [(0, 1)])

        self.player_field.flag_coords = [(2, 0)]
        self.player_field.toggle_flag(2, 0)
        self.assertEqual(self.player_field.flag_coords, [])

        self.assertRaises(ValueError, self.player_field.toggle_flag, 5, 5)

    def test_tile(self):
        self.player_field.field.mine_coords = [(0, 0), (1, 0)]
        self.player_field.open_coords = [(1, 1)]
        self.player_field.flag_coords = [(0, 0), (2, 1)]
        self.player_field.hints = {(0, 0): -1, (0, 1): 2, (0, 2): 0, (0, 3): 0,
                                   (1, 0): -1, (1, 1): 2, (1, 2): 0, (1, 3): 0,
                                   (2, 0): 1, (2, 1): 1, (2, 2): 0, (2, 3): 0,
                                   (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}

        actual = self.player_field.tile(1, 1)
        expected = {"hint": 2, "flag": False}
        self.assertEqual(actual, expected)

        actual = self.player_field.tile(0, 0)
        # Hint is None as the mine is not open
        expected = {"hint": None, "flag": True}
        self.assertEqual(actual, expected)

        actual = self.player_field.tile(1, 0)
        expected = {"hint": None, "flag": False}
        self.assertEqual(actual, expected)

    def test_nine_tiles(self):
        self.player_field.field.mine_coords = [(0, 0), (1, 0)]
        self.player_field.open_coords = [(1, 1), (0, 1)]
        self.player_field.flag_coords = [(0, 0), (2, 1)]

        # o: closed tile
        # [0-9]: open tile, hint
        # X: mine
        # ----------
        # o o o o
        # 0 o o o
        # 1 2 X o
        # X o o o

        actual = self.player_field.nine_tiles(0, 1)
        # Expect to exclude tiles outside the field.
        expected = {
                (0, 0): {"hint": None, "flag": True},
                (0, 1): {"hint": 1, "flag": False},
                (0, 2): {"hint": 0, "flag": False},
                (1, 0): {"hint": None, "flag": False},
                (1, 1): {"hint": 2, "flag": False},
                (1, 2): {"hint": None, "flag": False}
                }

        self.assertCountEqual(actual, expected)
