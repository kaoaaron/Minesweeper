import numpy as np
import random
import sys
import os

NUM_ROWS   = 8
NUM_COLS   = 8
NUM_MINES  = 10


#randomly initializes the game board
def initialize(seed):

	random.seed(seed) #random generator

	grid_linear = ([True] * NUM_MINES) + [False] * (NUM_ROWS * NUM_COLS - NUM_MINES) #create list with x True and y False values
	
	random.shuffle(grid_linear)

	grid = np.array(grid_linear)
	grid = grid.reshape(NUM_ROWS, NUM_COLS)

	return grid

#prints board
def print_full_board(grid, move_num):
	
	print("""
==========
Move %d
==========
	""" % move_num)
	
	print("  | 0 1 2 3 4 5 6 7"); print("-------------------")
	for r in range(NUM_ROWS):
		in_between = ""
		print("%d | " % r, end="")
		for c in range(NUM_COLS):
			print(in_between, grid[r,c], end="", sep="")
			in_between = " "
		print()
	
	return
	
#reveals board based on user input
def reveal_board_cell(game_grid, revealed_grid, row, col):
	
	counter = 0
	
	if revealed_grid[row,col] == -1:
		print("\nGame Over")
		print("""
==============================
REVEALED BOARD (-1 are Mines)		
==============================
		""")
		print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in revealed_grid]))
		
		ans = input("\n Would you like to play again [y][n]?  ")
		if ans == 'y':
			main()
		else:
			sys.exit()
	else:
		if revealed_grid[row][col] == 0:
			for x in range(row-1, row+2):
				for y in range(col-1, col+2):
					if x < 0 or y < 0 or x > NUM_ROWS-1 or y > NUM_COLS-1:
							continue
					game_grid[x,y] = revealed_grid[x,y]
		else:
			game_grid[row,col] = revealed_grid[row,col]
			
	return game_grid

#reveals entire board based on random init values
def revealed_board(mines_grid):

	counter = 0;
	revealed_grid = np.zeros(NUM_ROWS*NUM_COLS, dtype=int).reshape(NUM_ROWS,NUM_COLS)
	
	for x in range(0, NUM_ROWS):
		for y in range(0, NUM_COLS):
			if mines_grid[x,y] == True:
				revealed_grid[x,y] = -1
			else:
				for xx in range(x-1, x+2):
					for yy in range(y-1, y+2):
						if xx == x and yy == y or xx < 0 or yy < 0 or xx > NUM_ROWS-1 or yy > NUM_COLS-1:
							continue
						if mines_grid[xx,yy] == True:
							counter += 1
				revealed_grid[x,y] = counter
				counter = 0
	

	return revealed_grid
	
def main():

	move = 0
	
	#set up game board
	game_grid = ['*'] * (NUM_COLS * NUM_ROWS); game_grid = np.array(game_grid)
	game_grid = game_grid.reshape(NUM_ROWS, NUM_COLS)
	print_full_board(game_grid, move)
	

	if (len(sys.argv) > 1):
		seed = int(sys.argv[1])
	else:
		seed = random.randint(0,5000)

	mines_grid = initialize(seed)
	
	revealed_grid = revealed_board(mines_grid)
	
	while True:
		try:
			row, column = input("\nEnter Column and Row to Reveal: ").split(" ")
			row = int(row); column = int(column)
		except ValueError:
			print("""\n
Your input MUST consist of 2 numbers between 0-7 with EXACTLY one space between them.

VALID INPUTS INCLUDE:
0 3
7 7
	
INVALID INPUTS INCLUDE:
0     4
0   8
4
7 9
a
a k
				
PLEASE TRY AGAIN
			""")
			continue
		if row < 0 or column < 0 or row > NUM_ROWS-1 or column > NUM_COLS-1:
			print("""\n
Your input MUST consist of 2 numbers between 0-7 with EXACTLY one space between them.

VALID INPUTS INCLUDE:
0 3
7 7
	
INVALID INPUTS INCLUDE:
0     4
0   8
4
7 9
a
a k
				
PLEASE TRY AGAIN
			""")
			continue
		
		if game_grid[row,column] != "*":
			print("\nThis block is already unveiled. \nTry Another")
			continue
		move += 1
		game_grid = reveal_board_cell(game_grid, revealed_grid, row, column)
		print_full_board(game_grid, move)
		
		win_tracker = np.count_nonzero(game_grid == '*')
		if(win_tracker == NUM_MINES):
			print(""" 
              _.---..._
            ./^         ^-._
         ./^C===.         ^\.   /|
        .|'     \\        _ ^|.^.|
   ___.--'_     ( )  .      ./ /||
  /.---^T\      ,     |     / /|||
 C'   ._`|  ._ /  __,-/    / /-,||
      \ \/    ;  /O  / _    |) )|,
       i \./^O\./_,-^/^    ,;-^,'     
        \ |`--/ ..-^^      |_-^     
         `|  \^-           /|:     
          i.  .--         / '|.                                 
           i   =='       /'  |\._                         
         _./`._        //    |.  ^-ooo.._                     
  _.oo../'  |  ^-.__./X/   . `|    |#######b                  
 d####     |'      ^^^^   /   |    _\#######               
 #####b ^^^^^^^^--. ...--^--^^^^^^^_.d######                
 ######b._         Y            _.d######### 
 ##########b._     |        _.d#############            

			
			WINNER!""")
			
			ans = input("\n Would you like to play again [y][n]?  ")
			if ans == 'y':
				main()
			else:
				sys.exit()

		
		
print("""
__  __ _                                                   
|  \/  (_)_ __   ___  _____      _____  ___ _ __   ___ _ __ 
| |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
| |  | | | | | |  __/\__ \\ V  V /  __/  __/ |_) |  __/ |   
|_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   
                                           |_|              
This is a simplified version of the game Minesweeper

The goal of the game is to uncover all the tiles except for the mines

Rules:

1) Each tile has either 
	a) a number indicating # of surrounding bombs
	b) a bomb
	c) a blank space
2) Once a location on the grid is selected, two things can happen:
	a) the surrounding tiles are uncovered
	b) a bomb is selected -- GAME OVER
	
*Note: Columns and Rows Range from 0 - 7

""")


input("Press ENTER to begin...")
os.system("clear")
		
main()
