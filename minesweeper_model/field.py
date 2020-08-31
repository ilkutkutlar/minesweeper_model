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

class HintGenerator:
    @staticmethod
    def hints_for_field(field_width, field_height, mines):
        return {(x, y): HintGenerator.hint_for_tile(x, y, field_width, field_height, mines)
                for x in range(field_width) 
                for y in range(field_height)}

    @staticmethod
    def hint_for_tile(tile_x, tile_y, field_width, field_height, mines):
        """Return the hint for the given tile.

        Parameters:
            tile_x: X coord of tile
            tile_y: Y coord of tile
            field_with: width of Minesweeper field
            field_height: height of Minesweeper field
            mines (list of two-tuples): list of mine coords
        
        Returns:
            Number of mines in surrounding tiles (hint) 
            for the given tile, or -1 if tile being checked has a mine.
        """

        if (tile_x, tile_y) in mines:
            return -1
        
        # Loops generate all surrounding tiles and the tile itself
        surrounding_tiles = [(x, y) for x in [tile_x - 1, tile_x, tile_x + 1] 
                                    for y in [tile_y - 1, tile_y, tile_y + 1]]

        # Remove the tile we are checking to only leave surrounding tiles
        surrounding_tiles.remove((tile_x, tile_y))

        # No need to worry about edge cases caused by -ve tile coords in 
        # surrounding_tiles as the mines list simply won't have the -ve 
        # coords and those coords will register as False, as desired
        surrounding_tiles_have_mine = [(x, y) in mines for (x, y) in surrounding_tiles]

        return surrounding_tiles_have_mine.count(True)

