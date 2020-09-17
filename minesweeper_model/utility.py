def surrounding_tiles(tile_x, tile_y, remove_outside_tiles=False):

    """Return the 8 tiles surrounding the given tile.

    Parameters:
        tile_x: X coord of tile
        tile_y: Y coord of tile

    Returns:
        List of two tuples (x, y) of surrounding tiles.
        The list will exclude the given tile itself.
        The list can potentially contain -ve coordinates.
    """

    # Loops generate all surrounding tiles and the tile itself
    tiles = [
        (x, y)
        for x in [tile_x - 1, tile_x, tile_x + 1]
        for y in [tile_y - 1, tile_y, tile_y + 1]
    ]

    # Remove the tile itself to only leave surrounding tiles
    tiles.remove((tile_x, tile_y))

    if remove_outside_tiles:
        tiles = [(x, y) for (x, y) in tiles if x >= 0 and y >= 0]

    return tiles


def str_input_to_mine_coords(input_string):
    rows = input_string.split("\n")
    x_len, y_len = len(rows[0]), len(rows)

    mine_coords = []
    x_mine, y_mine = 0, 0

    for row in rows:
        x_mine = 0

        for col in row:
            if col == "x":
                mine_coords.append((x_mine, y_mine))
            x_mine += 1
        y_mine += 1

    return (x_len, y_len, mine_coords)
