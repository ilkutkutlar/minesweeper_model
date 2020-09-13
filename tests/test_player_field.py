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

        field3_mines = [(2, 0), (2, 2), (6, 3), (1, 5), (5, 6)]
        self.field3 = field.PlayerField(field.Field(8, 7, field3_mines))

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
        # .: closed tile
        # [0-9]: open tile, hint
        # x: mine
        # !: flag
        # ----------
        # ! . . .
        # 2 2 . .
        # x x . .
        # . . . .

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

    @unittest.skip("Not implemented")
    def test_open_tile_open_adjacent_tiles(self):
        # field3
        # mines:        hints:      expected open:
        #
        # ..x.....      01x10000    ..x+++++
        # ........      02220000    ...+++++
        # ..x.....      01x10111    ..x+++++
        # ......x.      011101x1    ...+++x.
        # ........      11100111    ..++++..
        # .x......      1x101110    .x+++...
        # .....x..      11101x10    ..+++x..

        self.field3.open_tile(5, 1, True)

        # expect adjacent 0 hint tiles to open recursively until a non-zero hint tile
        # is found, when the adjacent tiles are opened the last time and algorithm stops.
        expected_open_coords = [(3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                                (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                                (3, 3), (4, 3), (5, 3),
                                (2, 4), (3, 4), (4, 4), (5, 4),
                                (2, 5), (3, 5), (4, 5),
                                (2, 6), (3, 6), (4, 6)]
        self.assertEqual(self.field3.open_coords, expected_open_coords)

    def test_toggle_flag(self):
        self.field1.toggle_flag(0, 1)
        self.assertEqual(self.field1.flag_coords, [(0, 1)])

        self.field1.flag_coords = [(2, 0)]
        self.field1.toggle_flag(2, 0)
        self.assertEqual(self.field1.flag_coords, [])

        self.assertRaises(ValueError, self.field1.toggle_flag, 5, 5)

    def test_traverse_tiles(self):
        # ..x.....      01x10000
        # .....~..      02220~00
        # ..x.....      01x10111
        # ......x.      011101x1
        # ........      11100111
        # .x......      1x101110
        # .....x..      11101x10

        # Adjacent 0: [(4, 0), (4, 1), (4, 2), (5, 0), (6, 0), (6, 1)]

        def should_visit(x, y, player_field):
            return player_field.hints[(x, y)] == 0

        actual = self.field3.traverse_tiles(0, 0, should_visit)
        expected = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.assertEqual(actual, expected)

    def test_render(self):
        mines = [(0, 0), (3, 1), (0, 3)]
        f = field.Field(4, 4, mines)
        pf = field.PlayerField(f)
        pf.flag_coords = [(1, 1)]
        pf.open_coords = [(0, 1), (3, 3)]
        pf.hints = {(0, 1): 1, (3, 3): 0}

        expected = "....\n1!..\n....\n...0\n"
        self.assertEqual(pf.render(), expected)

        expected = "oooo\n1?oo\noooo\nooo0\n"
        self.assertEqual(pf.render("?", "o"), expected)
