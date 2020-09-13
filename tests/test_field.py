import unittest
from minesweeper_model import field


class TestField(unittest.TestCase):
    def test_are_coords_valid(self):
        f = field.Field(4, 4)
        self.assertTrue(f.are_coords_valid(3, 2))
        self.assertFalse(f.are_coords_valid(5, 2))

    def test_render(self):
        mines = {(0, 0), (3, 1), (1, 3)}
        f = field.Field(4, 4, mines)

        expected = "x...\n...x\n....\n.x..\n"
        self.assertEqual(f.render(), expected)

        expected = "@ooo\nooo@\noooo\no@oo\n"
        self.assertEqual(f.render("o", "@"), expected)
