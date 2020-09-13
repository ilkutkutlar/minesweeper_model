from minesweeper_model import generator, utility


class Field:
    def __init__(self, width, height, mine_coords=[]):
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
        self.open_coords = []
        self.flag_coords = []
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
        return {coords: self.tile(coords[0], coords[1])
                for coords in nine_tiles}

    def open_tile(self, x, y, open_adjacent_tiles=False):
        if (x, y) in self.field.mine_coords:
            return False
        else:
            self.open_coords.append((x, y))

            return True

    def toggle_flag(self, x, y):
        flag = (x, y)

        if not self.field.are_coords_valid(flag[0], flag[1]):
            raise ValueError("Invalid coordinate given: point out of field")

        if flag in self.flag_coords:
            self.flag_coords.remove(flag)
        else:
            self.flag_coords.append(flag)

    def traverse_adjacent_tiles(self, x, y, get_adjacent_tiles, visited=[]):

        """Recursively traverse selected adjacent tiles of a given starting tile.
        Which adjacent tiles to traverse are selected by the given get_adjacent_tiles method.

        Parameters:
            x: X coord of starting tile
            y: Y coord of starting tile
            get_adjacent_tiles: function which accepts (x, y, field, player_field)
                Returns a list of tiles adjacent to (x, y) which should be traversed.
            visited: Already visited tiles; used for recursion.

        Returns:
            A list of all adjacent tiles found which were selected by the given method.
        """

        # This implementation uses DFS traversal.
        visited.append((x, y))

        adjacent = get_adjacent_tiles(x, y, self.field, self)
        adjacent_not_visited = list(filter(lambda t: t not in visited, adjacent))

        # Tiles that lay underneath this level of the "tree"
        tiles_below = [(x, y)]

        for adj_x, adj_y in adjacent_not_visited:
            tiles_below_adj = self.traverse_adjacent_tiles(adj_x, adj_y, get_adjacent_tiles, visited)
            tiles_below.extend(tiles_below_adj)

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

    def _adjacent_zero_hint_tiles(self, x, y):
        adjacent_tiles = utility.surrounding_tiles(x, y, True)
        return [tile for tile in adjacent_tiles if self.hints[tile] == 0]

    def __str__(self):
        return self.render()
