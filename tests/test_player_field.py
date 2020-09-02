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
