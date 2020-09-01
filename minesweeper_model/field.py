from minesweeper_model import generator


class Field:
    def __init__(self, width, height, mine_coords=[]):
        self.width = width
        self.height = height

        self.mine_coords = mine_coords
        self.hints = generator.hints_for_field(width, height, mine_coords)

        self.flag_coords = []
        self.open_coords = []

    def toggle_flag(self, x, y):
        flag = (x, y)

        if not self._are_coords_valid(flag[0], flag[1]):
            raise ValueError("Invalid coordinate given: point out of field")

        if flag in self.flag_coords:
            self.flag_coords.remove(flag)
        else:
            self.flag_coords.append(flag)

    def surrounding_hints(self, x, y):
        pass

    def open_tile(self, x, y):
        pass

    def _are_coords_valid(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)


if __name__ == "__main__":
    f = Field(5, 5, generator.random_mine_coords(5, 5, 5))
    print(f.hints)
