def surrounding_tiles(tile_x, tile_y):
    # Loops generate all surrounding tiles and the tile itself
    tiles = [(x, y) for x in [tile_x - 1, tile_x, tile_x + 1]
             for y in [tile_y - 1, tile_y, tile_y + 1]]

    # Remove the tile itself to only leave surrounding tiles
    tiles.remove((tile_x, tile_y))

    return tiles
