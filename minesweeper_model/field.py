from minesweeper_model import generator


class Field:
    def __init__(self, width, height, mine_coords=[]):
        self.width = width
        self.height = height
        self.mine_coords = mine_coords

    def are_coords_valid(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)


class PlayerField:
    def __init__(self, field):
        self.field = field
        self.open_coords = []
        self.flag_coords = []
        self.hints = generator.hints_for_field(
                     field.width, field.height, field.mine_coords)

    def open_tile(self, x, y):
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
