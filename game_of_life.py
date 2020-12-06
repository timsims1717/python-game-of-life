from graphics import *
import time

WIDTH = 64
HEIGHT = 48

### a single cell in the Game of Life Grid
### Knows its coords, whether it is alive or should be alive,
### its rectangle object and whether that rectangle is being drawn
class Cell:
	x = 0
	y = 0
	alive = False
	should = False
	rec = None
	drawn = False

	def __init__(self, x, y, a):
		r = Rectangle(Point(x, y), Point(x + 1, y + 1))
		r.setFill("black")
		self.alive = a
		self.x = x
		self.y = y
		self.rec = r

### Creates a window and initializes the grid with a glider
### Starts the game loop
def main():
	win = GraphWin(title = "Game of Life", width = 640, height = 480)
	win.setCoords(0, 0, WIDTH, HEIGHT)

	grid = generate_grid()
	grid[0][2].alive = True
	grid[1][0].alive = True
	grid[1][2].alive = True
	grid[2][1].alive = True
	grid[2][2].alive = True
	# print_grid(grid)
	# print_live_adj(grid)
	# print_should_live(grid)
	draw_grid(win)
	game_loop(win, grid)

### Updates the grid if the simulation is stepping
### Checks for key presses and mouse clicks
def game_loop(win, grid):
	stepping = False
	speed = 0.1
	mouseDown = False
	while True:
		if stepping:
			time.sleep(speed)
			update_grid(grid)
		draw_cells(win, grid)
		input = win.checkKey()
		# if input != "":
		# 	print(input)
		if input == "space":
			# toggle whether the simulation is stepping or not
			stepping = not stepping
		elif input == "plus" or input == "equal" or input == "KP_Add":
			# double the speed
			speed /= 2.0
		elif input == "minus" or input == "underscore" or input == "KP_Subtract":
			# halve the speed
			speed *= 2.0
		elif input == "Escape" or input == "q" or input == "Q":
			# quit the program
			return
		m_input = win.checkMouse()
		if m_input:
			# Toggle a cell to be alive or dead
			x = int(m_input.getX())
			y = int(m_input.getY())
			grid[y][x].alive = not grid[y][x].alive

### Draw the grid to the window
def draw_grid(win):
	for i in range(1, WIDTH):
		r = Rectangle(Point(i, 0), Point(i, HEIGHT))
		r.draw(win)
	for i in range(1, HEIGHT):
		r = Rectangle(Point(0, i), Point(WIDTH, i))
		r.draw(win)

### Check all cells to see whether they need to be drawn or undrawn
def draw_cells(win, grid):
	for y, row in enumerate(grid):
		for x, cell in enumerate(row):
			if cell.alive:
				if not cell.drawn:
					cell.rec.draw(win)
					cell.drawn = True
			else:
				if cell.drawn:
					cell.rec.undraw()
					cell.drawn = False

### Returns whether a cell should be alive in the next iteration
### Rules (from https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):
###   Any live cell with two or three live neighbors survives
###   Any dead cell with three live neighbors becomes a live cell
###   All other live cells die in the next generation. Similarly, all other dead cells stay dead
def should_live(grid, x, y):
	count = get_live_adj(grid, x, y)
	live = grid[y][x].alive
	if live:
		return count == 3 or count == 2
	else:
		return count == 3

### Counts the number of live cells adjacent to the input cell
def get_live_adj(grid, x, y):
	count = 0
	for i in range(y-1, y+2):
		if i >= 0 and i < len(grid):
			for j in range(x-1, x+2):
				if j >= 0 and j < len(grid[i]):
					if grid[i][j].alive and (i != y or j != x):
						count += 1
	return count

### For each cell, checks whether it should live or die
### Then updates each cell
def update_grid(grid):
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			grid[i][j].should = should_live(grid, j, i)
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			grid[i][j].alive = grid[i][j].should

### Prints the grid to the terminal
def print_grid(grid):
	for row in grid:
		for cell in row:
			if cell.alive:
				print('A', end=' ')
			else:
				print('.', end=' ')
		print()
	print()

### Prints the grid as a count of adjacent live cells to the terminal
def print_live_adj(grid):
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			count = get_live_adj(grid, j, i)
			print(count, end=' ')
		print()
	print()

### Prints the grid as whether a cell should live or not in the next generation
def print_should_live(grid):
	for i, row in enumerate(grid):
		for j, cell in enumerate(row):
			live = should_live(grid, j, i)
			if live:
				print('L', end=' ')
			else:
				print('D', end=' ')
		print()
	print()

### Creates the grid with all dead cells
def generate_grid():
	grid = []
	for y in range(HEIGHT):
		grid.append([])
		for x in range(WIDTH):
			grid[y].append(Cell(x, y, False))
	return grid

main()