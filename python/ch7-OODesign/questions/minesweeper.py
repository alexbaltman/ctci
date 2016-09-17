'''
Design and implement a text-based Minesweeper game. Minesweeper is the classic single-player computer game where an NxN grid has B mines (or bomobs) hidden across the grid. The remaining cells are either blank or have a number behind them. The numbers reflect the number of bombs in the surrounding eight cells. The user then uncovers a cell. If it is a bomb, the player loses. If it is a number, the number is exposed. If it is a blank cell, this cell and all adjacent blank cells (up to and including the surrounding numeric cells) are exposed. The player winds when all non-bomb cells are exposed. The player can also flag certain places as potential bombs. This doesn't affect game play, other than to block the user from accidentally clicking a cell that is thought to have a bomb.

(Tip for the reader: if you're not familiar with this game, please play a few rounds online first.)

e = empty/blank

Fully exposed board w/ 3 bombs. This is not shown to the user.
e 1 1 1 e e e
e 1 * 1 e e e
e 2 2 2 e e e
e 1 * 1 e e e
e 1 1 1 e e e
e e e 1 1 1 e
e e e 1 * 1 e

Clicking on the cell (row = 1, col = 0) would expose this:
e 1 ? ? ? ? ?
e 1 ? ? ? ? ?
e 2 ? ? ? ? ?
e 1 ? ? ? ? ?
e 1 1 1 ? ? ?
e e e 1 ? ? ?
e e e 1 ? ? ?

The user winds when everything other than bombs has been exposed.
e 1 1 1 e e e
e 1 ? 1 e e e
e 2 2 2 e e e
e 1 ? 1 e e e
e 1 1 1 e e e
e e e 1 1 1 e
e e e 1 ? 1 e

Hints: 351, 361, 377, 386, 399
'''


def minesweeper(s):
    pass

if __name__ == '__main__':
    assert minesweeper('') ==
    assert minesweeper('') ==
    assert minesweeper('') ==
    assert minesweeper('') ==
    assert minesweeper('') ==
