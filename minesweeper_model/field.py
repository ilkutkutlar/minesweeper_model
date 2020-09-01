class Field:
    def __init__(self, width, height, mine_coords=[]):
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
