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

This package offers a `Field` class which models a minefield in a Minefield game. It stores all the necessary state of a field: the open tiles, flagged tiles, tiles with a mine under it, etc. By the rules of the game, the player isn't allowed to know where the mines are hidden.

The `Field` class has methods to allow interacting with it as a player (i.e. you are only given hints, the number of mines surrounding a tile, but not the mine locations). However, of course, direct access to mine locations are possible if desired as well.

### Initialization

```py
from minesweeper_model import field

# Mine locations are expressed as two-tuples (x, y)
# The top-left tile in the minefield has coordinates (0, 0).
# Mine locations argument is optional, so a field without mines
# is theoretically possible.
mine_coords = [(0, 0), (1, 0)]
field = field.Field(5, 5, mine_coords)
```

### Data stored in the `Field` class

```py
# List of tuples (x, y) of mine coordinates.
field.mine_coords

# List of tuples (x, y) of coordinates which have been opened by the player.
field.open_coords

# List of tuples (x, y) of coordinates which have been flagged as having a mine.
field.flag_coords

# Dictionary populated with the "hint" for all tiles in the Field given
# during initialization of the `PlayerField` class. This is the number 
# of mines in the surrounding 8 tiles for each tile. Dictionary is in the 
# format `{(x, y): int}` where int is the hint with possible values 
# being 0 to 8 or -1 (for tiles which have mines underneath)
field.hints
```

### Interact with the `Field` class

Use the `tile` and `nine_tiles` methods to get information about a single field and a group of nine fields respectively. You will only receive the information a player would get (i.e. anything but the location of mines)

```py
# Return a dictionary {"hint": int, "flag": bool} where
# "hint" is the hint revealed by openning the tile, or
# the value None if the tile is closed. "flag" is whether
# the tile is flagged.
field.tile(x, y)

# Returns the same data as `tile` method for the given
# tile as well as the 8 tiles surrounding it.
# Data is returned in format: {(x, y): {"hint": int, "flag": bool}, ...}
field.nine_tiles(middle_x, middle_y)
```

Open tiles and place flags in the field:

```py
# This will open the tile in given coordinates. Will return
# True if tile does not hide a mine, False otherwise.
# If tile has no mine, given coordinates will be added to open_coords.
field.open_tile(x, y)

# Pass True to the third coordinate so that in addition to the given tile
# being opened, all the adjacent tiles with a hint of 0 will also be opened,
# similar to the way it does in some versions of the Minesweeper game. 
field.open_tile(x, y, True)

# Add or remove flag on tile.
field.toggle_flag(x, y)
```

### Visual representation of fields

Draw the field showing mine locations:

```py
print(field.render_mines())

# x...
# ...x
# ....
# .x..

# You can use custom strings when drawing
print(field.render_mines(tile_str="o", mine_str="@"))

# @ooo
# ooo@
# oooo
# o@oo
```

Draw the field a player would see, only showing hints and flags but not mines:

```py
print(field.render_player_field())

# !...
# 22..
# xx..
# ....

# You can use custom strings when drawing
print(player_field.render_player_field(flag_str="?", closed_str="o"))

# ?ooo
# 22oo
# xxoo
# oooo
```

### Generator utilities

The package also contains utilities to help you generate minefields.

Generate N many mine locations randomly for a given field size:

```py
from minesweeper_model import generator

# generate 4 mine coordinates 
# for a field of size (5, 10)
generator.random_mine_coords(5, 10, 4)

# => [(1, 5), (3, 2), (0, 0), (1, 6)]
```

Generate hint for a single tile given a list of mine coordinates:

```py
mines = [(4, 1), (6, 4)]

# Generate hint for a tile at (1, 1)
generator.hint_for_tile(1, 1, mines):

# => 0
```

Generate hints for an entire field:

```py
mines = [(4, 1), (6, 4)]

# Generate hints for a field of size (10, 10)
generator.hints_for_field(10, 10, mines)

# => {(0, 0): 0, (0, 1): 0, ... , (9, 9): 0}
```

### General utilities

Get coordinates of surrounding tiles:

```py
from minesweeper_model import utility

utility.surrounding_tiles(1, 1)

# => [(0, 0), (0, 1), (0, 2), (1, 0), 
#     (1, 2), (2, 0), (2, 1), (2, 2)]

# If the tile is on the edge, method will
# return -ve coordinates as well.
utility.surrounding_tiles(0, 0)

# => [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
#     (0, 1), (1, -1), (1, 0), (1, 1)]

# You can choose to remove -ve coordinates:
utility.surrounding_tiles(0, 0, True)

# => [(0, 1), (1, 0), (1, 1)]
```

Convert a textual representation of a field to parameters you can pass to a `Field` object as an easier way of creating fields (Thanks to <a href="https://github.com/27Anurag">@27Anurag</a> for the contribution):

```py
str_field = """..x...x
.......
....x..
......x
x......"""

width, height, mine_coords = utility.str_input_to_mine_coords(str_field)

# => width: 7, height: 5, mine_coords: [(2, 0), (6, 0), (4, 2), (6, 3), (0, 4)]
f = field.Field(width, height, mine_coords)
```

## Development

- The package currently only officially supports `python3`.
- Tests are written with `unittest` and are under the "tests" directory. You can run all tests on the command line with `python3 -m unittest`.
- <a href="https://flake8.pycqa.org/en/latest/">`flake8`</a> is used for checking the code follows some Python best practices and styling standards. You can run the checks on the command line with `flake8` (need to install flake8 first).
- <a href="https://tox.readthedocs.io/en/latest/">tox</a> is used to automate testing. You can run all tests and checks (e.g. flake8) on the command line with `tox` (need to install tox first).
