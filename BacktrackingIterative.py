from BacktrackingClasses import Vacuum, Maze

class PathNode:
    def __init__(this, r, c, dir, depth):
        this.r = r
        this.c = c
        this.entry_dir = dir
        this.depth = depth

def solve_maze_iterative(vacuum, max_depth):
    visited = set()
    path_stack = []
    
    path_stack.append(PathNode(vacuum.row, vacuum.col, vacuum.direction, 0))
    visited.add((vacuum.row, vacuum.col))

    while path_stack:
        curr_depth = path_stack[-1].depth
        moved_this_turn = False

        if curr_depth < max_depth:
            for _ in range(4):
                front_cell = vacuum.see()
                
                if front_cell == Maze.SALIDA:
                    vacuum.move_forward()
                    return True
                
                increments_row, increments_col = Vacuum.DIR_OPS[vacuum.direction]
                next_row, next_col = vacuum.row + increments_row, vacuum.col + increments_col
                
                if front_cell in (Maze.VACIO, Maze.ENTRADA) and (next_row, next_col) not in visited:
                    vacuum.move_forward()
                    visited.add((next_row, next_col))
                    path_stack.append(PathNode(next_row, next_col, vacuum.direction, curr_depth + 1))
                    moved_this_turn = True
                    break
                vacuum.turn_left()

        if not moved_this_turn:
            entry_dir = path_stack.pop().entry_dir
            if path_stack:
                while vacuum.direction != entry_dir:
                    vacuum.turn_left()
                vacuum.backtrack_movement()

    return False