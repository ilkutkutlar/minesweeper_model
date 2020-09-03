import random
from minesweeper_model import helper


def random_mine_coords(field_width, field_height, mine_count):
    random.seed()
    all_field_coords = [(x, y) for x in range(field_width)
                        for y in range(field_height)]
    return random.sample(all_field_coords, mine_count)


def hints_for_field(field_width, field_height, mines):
    return {(x, y): hint_for_tile(x, y, mines)
            for x in range(field_width)
            for y in range(field_height)}


def hint_for_tile(tile_x, tile_y, mines):

    """Return the hint for the given tile.

    Parameters:
        tile_x: X coord of tile
        tile_y: Y coord of tile
        mines (list of two-tuples): list of mine coords

    Returns:
        Number of mines in surrounding tiles (hint)
        for the given tile, or -1 if tile being checked has a mine.
    """

    if (tile_x, tile_y) in mines:
        return -1

    surrounding_tiles = helper.surrounding_tiles(tile_x, tile_y)

    # No need to worry about edge cases caused by -ve tile coords in
    # surrounding_tiles as the mines list simply won't have the -ve
    # coords and those coords will register as False, as desired
    surrounding_tiles_have_mine = [(x, y) in mines for (x, y) in surrounding_tiles]

    return surrounding_tiles_have_mine.count(True)
