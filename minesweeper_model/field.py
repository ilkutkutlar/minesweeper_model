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

def hint_for_tile(tile_x, tile_y, field_width, field_height, mines):
    """Return the hint for the given tile.

    Parameters:
        tile_x: X coord of tile
        tile_y: Y coord of tile
        field_with: width of Minesweeper field
        field_height: height of Minesweeper field
        mines (list of two-tuples): list of mine coords
    
    Returns:
        Hint for the given tile.
    """

    def is_mine(x, y):
        # is tile outside the bounds of the Minesweeper field?
        is_outside_bottom_left = (x < 0) or (y < 0)
        is_outside_top_right = (x > field_width - 1) or (y > field_height - 1)

        if is_outside_bottom_left:
            return False
        elif is_outside_top_right:
            return False
        else:
            return (x, y) in mines
    
    surrounding_tiles = [
        (tile_x - 1, tile_y + 1), (tile_x, tile_y + 1), (tile_x + 1, tile_y + 1),
        (tile_x - 1, tile_y), (tile_x + 1, tile_y),
        (tile_x - 1, tile_y - 1), (tile_x, tile_y - 1), (tile_x + 1, tile_y - 1)
    ]

    surrounding_tile_mines = [is_mine(x, y) for x, y in surrounding_tiles]
    return surrounding_tile_mines.count(True)

