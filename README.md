# Minesweeper Model

[![PyPI Version](https://img.shields.io/pypi/v/minesweeper-model)](https://pypi.org/project/minesweeper-model/)

This package is a <a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)">Minesweeper game</a> without a frontend. In other words, it only offers a Minesweeper model and an interface to access and modify the minefield or "play" the game programmatically. As a result, this package is not meant to be a Minesweeper game playable by an end user.

This package is mostly meant for people who develop Minesweeper solvers. Anyone developing such a solver can use this package to skip the step of developing a Minesweeper model to test their solver on and start working on the solver itself straightaway.

## Installation

The package is hosted on <a href="https://pypi.org/project/minesweeper-model/">PyPI</a>. You can install it with `pip`:

```sh
pip install minesweeper-model
```

## Usage

This package offers two field classes: `Field` and `PlayerField`. `Field` is the actual minefield storing the location of mines. By the rules of the game, the player isn't supposed to have access to this.

`PlayerField` is the minefield that the player is allowed to access: It doesn't (directly) reveal the location of mines, but lets you see hints (number of mines in surrounding tiles) and flags you put as a player.

### Initialization

```py
from minesweeper_model import field

# Mine locations are expressed as two-tuples (x, y)
# The top-left tile in the minefield has coordinates (0, 0).
mine_coords = [(0, 0), (1, 0)]
real_field = field.Field(5, 5, mine_coords)

# Give the real field to PlayerField, so it can compute
# hints and report failure if a mine tile is opened.
player_field = field.PlayerField(real_field)
```

### Interact with the field as a player

Use `PlayerField` object to request information about the field and only receive what the player is allowed to know about (i.e. anything except the locationg of mines):

```py
# Return a dictionary {"hint": int, "flag": bool} where
# "hint" is the hint revealed by openning the tile, or
# the value None if the tile is closed. "flag" is whether
# the tile is flagged.
player_field.tile(x, y)

# Returns the same data as `tile` method for the given
# tile as well as the 8 tiles surrounding it.
# Data is returned in format: {(x, y): {"hint": int, "flag": bool}, ...}
player_field.nine_tiles(middle_x, middle_y)
```

Change the field in ways allowed for a player:

```py
# This will open the tile in given coordinates. Will return
# True if tile does not hide a mine, False otherwise.
# If tile has no mine, given coordinates will be added to open_coords.
# Unlike some Minesweeper games, this won't open adjacent tiles with a hint of 0.
player_field.open_tile(x, y)

# Add or remove flag on tile.
player_field.toggle_flag(x, y)
```

### Direct access to field data

PlayerField keeps coordinates of three objects:

#### 1. Hints

Dictionary populated with the "hint" for all tiles in the Field given during initialization of the `PlayerField` class. This is the number of mines in the surrounding 8 tiles for each tile. Dictionary is in the format `{(x, y): int}` where int is the hint with possible values being 0 to 8 or -1 (for tiles which have mines underneath):

```py
player_field.hints
```

#### 2. Open coordinates

List of tuples (x, y) of coordinates which have been opened by the player:

```py
player_field.open_coords
```

#### 3. Flag coordinates

List of tuples (x, y) of coordinates which have been flagged as having a mine:

```py
player_field.flag_coords
```

### Visual representation of fields

Draw the real field showing mine locations:

```py
print(real_field.render())

# x...
# ...x
# ....
# .x..

# You can use custom strings when drawing
print(player_field.render(tile_str="o", mine_str="@"))

# @ooo
# ooo@
# oooo
# o@oo
```

Draw player field, only showing hints and flags but not mines:

```py
print(player_field.render())

# !...
# 22..
# xx..
# ....

# You can use custom strings when drawing
print(player_field.render(flag_str="?", closed_str="o"))

# ?ooo
# 22oo
# xxoo
# oooo
```

### Generator utilities

The package also contains utilities to help you generate minefields.

Generate N many mine locations randomly for a given field size:

```py
# generate 4 mine coordinates 
# for a field of size (5, 10)
random_mine_coords(5, 10, 4)

# => [(1, 5), (3, 2), (0, 0), (1, 6)]
```

Generate hint for a single tile given a list of mine coordinates:

```py
mines = [(4, 1), (6, 4)]

# Generate hint for a tile at (1, 1)
hint_for_tile(1, 1, mines):

# => 0
```

Generate hints for an entire field:

```py
mines = [(4, 1), (6, 4)]

# Generate hints for a field of size (10, 10)
hints_for_field(10, 10, mines)

# => {(0, 0): 0, (0, 1): 0, ... , (9, 9): 0}
```

### General utilities

Get coordinates of surrounding tiles:

```py
surrounding_tiles(1, 1)

# => [(0, 0), (0, 1), (0, 2), (1, 0), 
#     (1, 2), (2, 0), (2, 1), (2, 2)]

# If the tile is on the edge, method will
# return -ve coordinates as well.
surrounding_tiles(0, 0)

# => [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
#     (0, 1), (1, -1), (1, 0), (1, 1)]

# You can choose to remove -ve coordinates:
surrounding_tiles(0, 0, True)

# => [(0, 1), (1, 0), (1, 1)]
```
