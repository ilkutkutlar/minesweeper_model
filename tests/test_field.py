import unittest
from minesweeper_model import field


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = field.Field(8, 8)

    def test_toggle_flag(self):
        self.field.toggle_flag(4, 5)
        self.assertEqual(self.field.flag_coords, [(4, 5)])

        self.field.flag_coords = [(6, 3)]
        self.field.toggle_flag(6, 3)
        self.assertEqual(self.field.flag_coords, [])

        self.assertRaises(ValueError, self.field.toggle_flag, 10, 10)
