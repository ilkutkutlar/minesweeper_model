class Field:
    def __init__(self, width, height, mine_coords = []):
        self.width = width
        self.height = height
        self.mine_coords = mine_coords
        self.flag_coords = []
        self.open_coords = []
        self.hints = []

    def place_flag(x, y):
        pass

    def open_tile(x, y):
        pass

def generate_hints(width, height, mines):
    pass

def hint_for_tile(x, y, mines):
    return 1

