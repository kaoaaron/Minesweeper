# Please change the two comment lines below to indicate your name &
# student number.
# Name: Jocelyn Krauthammer
# Student #: V00654320

import numpy as np
import random
import sys

DEBUG_SEED = 200
NUM_ROWS   = 8
NUM_COLS   = 8
NUM_MINES  = 10


def initialize(seed):
    """
    function: initialize
   
    Given an integer used to seed the random-number generator,
    create a NumPy array with NUM_ROWS rows and NUM_COLS columns
    where the value of True as any row/column means a mine is
    at that location, while False means there is no machine at
    that location.
       
    Input:
    ------
   
    * seed: integer value used to start up the random-number 
      generator. (The sequence of random numbers generated from
      the same seed never differs.) 
      
    Outputs:
    --------
    * A NumPy array with NUM_ROWS rows and NUM_COLS columns with
    * a dtype of bool.
    """
    random.seed(seed)

    # Start by making list NUM_ROWS * NUM_COLS booleans, with the
    # first NUM_MINES booleans equal to True, and the remainder
    # equal to False.

    grid_linear = ([True] * NUM_MINES) +  \
        [False] * (NUM_ROWS * NUM_COLS - NUM_MINES)

    # Now use Python's random module to shuffle this linear list
    random.shuffle(grid_linear)

    # Use NumPy to first create a one-dimensional array of the list,
    # and then change that one-dimensional array into a
    # two-dimensional array (with both arrays have the same number
    # of elements, but simply arranged differently).

    grid = np.array(grid_linear)
    grid = grid.reshape(NUM_ROWS, NUM_COLS)

    return grid


# You will need to modify this function header as part of
# your completion of the whole function.
def print_full_board(grid):
    return


# You will need to modify this function header as part of
# your completion of the whole function.
def reveal_board_cell(reveal_grid, row, col):
    return


def main():
    if (len(sys.argv) > 1):
        seed = int(sys.argv[1])
    else:
        seed = DEBUG_SEED 

    mines_grid = initialize(seed)


main()
