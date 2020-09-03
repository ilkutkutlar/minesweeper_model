import unittest
from minesweeper_model import field


class TestField(unittest.TestCase):
    def test_are_coords_valid(self):
        f = field.Field(4, 4)
        self.assertTrue(f.are_coords_valid(3, 2))
        self.assertFalse(f.are_coords_valid(5, 2))
