import unittest
from minesweeper_model.field import *

class TestField(unittest.TestCase):
    def test_generate_hints(self):
        self.assertEqual(hint_for_tile(0,0,0), 0)
