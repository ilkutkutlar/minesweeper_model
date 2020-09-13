from minesweeper_model import generator, utility


class Field:
    def __init__(self, width, height, mine_coords=set()):
        self.width = width
        self.height = height
        self.mine_coords = mine_coords

    def are_coords_valid(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)

    def render(self, tile_str=".", mine_str="x"):
        string = ""

        for y in range(self.height):
            for x in range(self.width):
                string += mine_str if (x, y) in self.mine_coords else tile_str
            string += "\n"

        return string

    def __str__(self):
        return self.render()


class PlayerField:
    def __init__(self, field):
        self.field = field
        self.open_coords = set()
        self.flag_coords = set()
        self.hints = generator.hints_for_field(
                     field.width, field.height, field.mine_coords)

    def tile(self, x, y):
        if (x, y) in self.open_coords:
            return {"hint": self.hints[(x, y)],
                    "flag": False}
        else:
            flag = (x, y) in self.flag_coords
            return {"hint": None,
                    "flag": flag}

    def nine_tiles(self, middle_x, middle_y):
        nine_tiles = utility.surrounding_tiles(middle_x, middle_y, True) + [(middle_x, middle_y)]
        return {(x, y): self.tile(x, y) for (x, y) in nine_tiles}

    def open_tile(self, x, y, open_adjacent_tiles=False):
        if (x, y) in self.field.mine_coords:
            return False
        else:
            self.open_coords.add((x, y))

            if open_adjacent_tiles:
                self._open_adjacent_zero_hint_tiles(x, y)

            return True

    def toggle_flag(self, x, y):
        flag = (x, y)

        if not self.field.are_coords_valid(flag[0], flag[1]):
            raise ValueError("Invalid coordinate given: point out of field")

        if flag in self.flag_coords:
            self.flag_coords.remove(flag)
        else:
            self.flag_coords.add(flag)

    def traverse_tiles(self, x, y, should_visit, visited=set()):

        """Traverse all selected tiles starting from a given tile. A given method is used
        to determine which of the surrounding tiles will be visited next during traversal.
        Traversal ends when none of the surrounding tiles have been selected to be visited next.

        Parameters:
            x: X coord of starting tile
            y: Y coord of starting tile
            should_visit: function which accepts (x, y, player_field)
                Returns a boolean of whether given tile should be visited.
            visited: Already visited tiles; used for recursion.

        Returns:
            A list of all tiles visited during traversal.
        """

        # This implementation uses DFS traversal.
        visited.add((x, y))

        all_surrounding = utility.surrounding_tiles(x, y, True)
        tiles_to_visit = [(x, y) for (x, y) in all_surrounding if should_visit(x, y, self)]
        tiles_to_visit = [t for t in tiles_to_visit if t not in visited]

        # Tiles that lay underneath this level of the "tree"
        tiles_below = {(x, y)}

        for (adj_x, adj_y) in tiles_to_visit:
            tiles_below_adj = self.traverse_tiles(adj_x, adj_y, should_visit, visited)
            tiles_below.update(tiles_below_adj)

        return tiles_below

    def render(self, flag_str="!", closed_str="."):
        string = ""

        for y in range(self.field.height):
            for x in range(self.field.width):
                tile = (x, y)

                if tile in self.flag_coords:
                    string += flag_str
                elif tile in self.open_coords:
                    string += str(self.hints[tile])
                else:
                    string += closed_str

            string += "\n"

        return string

    def _open_adjacent_zero_hint_tiles(self, x, y):
        def should_visit(x, y, player_field):
            return player_field.hints.get((x, y)) == 0

        adj_zero_hint_tiles = self.traverse_tiles(x, y, should_visit)

        # We've found zero-hint tiles above. These zero-hint tiles are arranged
        # contiguously on the minefield and form an area. Lastly, we need to
        # also open the tiles surrounding the tiles on the edge of this area.
        # Instead of finding the edge tiles, we can find and open the
        # surrounding tiles of all tiles within the area to have the same effect.

        all_surrounding_tiles = set()
        for (x, y) in adj_zero_hint_tiles:
            all_surrounding_tiles.update(utility.surrounding_tiles(x, y, True))

        valid_surrounding_tiles = {(x, y) for (x, y) in all_surrounding_tiles
                                   if self.field.are_coords_valid(x, y)}

        self.open_coords.update(adj_zero_hint_tiles)
        self.open_coords.update(valid_surrounding_tiles)

    def __str__(self):
        return self.render()
