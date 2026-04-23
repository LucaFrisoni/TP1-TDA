import random

class Maze:
    def __init__(this, grid):
        this.grid = grid
        this.rows = len(grid)
        this.cols = len(grid[0])

    def get_cell(this, r, c):
        if 0 <= r < this.rows and 0 <= c < this.cols:
            return this.grid[r][c]
        return 'X'

class Vacuum:
    DIR_OPS = {
        0: (-1, 0),     # Arriba
        1: (0, -1),     # Izquierda
        2: (1, 0),      # Abajo
        3: (0, 1)       # Derecha
    }

    def __init__(this, maze, start_row, start_col, start_dir=0):
        this.maze = maze
        this.row = start_row
        this.col = start_col
        this.direction = start_dir
        this.ops_count = 0
        this.backtrack_count = 0

    def turn_left(this):
        this.direction = (this.direction + 1) % 4
        this.ops_count += 1

    def move_forward(this):
        increments_row, increments_col = this.DIR_OPS[this.direction]
        this.row += increments_row
        this.col += increments_col
        this.ops_count += 1

    def see(this):
        this.ops_count += 1
        increments_row, increments_col = this.DIR_OPS[this.direction]
        look_row = this.row + increments_row
        look_col = this.col + increments_col
        return this.maze.get_cell(look_row, look_col)
        
    def backtrack_movement(this):
        this.turn_left()
        this.turn_left()
        this.move_forward()
        this.turn_left()
        this.turn_left()
        this.backtrack_count += 1
