import unittest
from minesweeper_model import field


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = field.Field(4, 4)

    def test_toggle_flag(self):
        self.field.toggle_flag(0, 1)
        self.assertEqual(self.field.flag_coords, [(0, 1)])

        self.field.flag_coords = [(2, 0)]
        self.field.toggle_flag(2, 0)
        self.assertEqual(self.field.flag_coords, [])

        self.assertRaises(ValueError, self.field.toggle_flag, 5, 5)

    def test_surrounding_hints(self):
        self.field.mines = [(0, 0), (3, 2), (1, 0), (2, 1)]

        # ....
        # ...X
        # ..X.
        # XX..

        self.assertEqual(self.field.surrounding_hints(0, 3), 0)
        self.assertEqual(self.field.surrounding_hints(3, 0), 1)
        self.assertEqual(self.field.surrounding_hints(1, 1), 3)
        # This tile has a mine
        self.assertEqual(self.field.surrounding_hints(0, 0), 1)

