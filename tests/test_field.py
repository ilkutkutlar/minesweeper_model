import unittest
from minesweeper_model import field


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = field.Field(4, 4)

    def test_are_coords_valid(self):
        self.assertTrue(self.field.are_coords_valid(3, 2))
        self.assertFalse(self.field.are_coords_valid(5, 2))
