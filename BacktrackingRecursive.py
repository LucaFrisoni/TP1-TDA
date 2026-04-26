from BacktrackingClasses import Vacuum, Maze

def solve_maze_recursive(vacuum, max_depth):
    visited = set()
    visited.add((vacuum.row, vacuum.col))
    
    def explore(current_depth):
        if current_depth >= max_depth:
            return False
            
        for _ in range(4):
            front_cell = vacuum.see()
            
            if front_cell == Maze.SALIDA:
                vacuum.move_forward()
                return True
                
            increments_row, increments_col = Vacuum.DIR_OPS[vacuum.direction]
            next_row, next_col = vacuum.row + increments_row, vacuum.col + increments_col
            
            if front_cell in (Maze.VACIO, Maze.ENTRADA) and (next_row, next_col) not in visited:
                entry_dir = vacuum.direction
                vacuum.move_forward()
                visited.add((next_row, next_col))
                
                if explore(current_depth + 1):
                    return True 
                    
                while vacuum.direction != entry_dir:
                    vacuum.turn_left()
                    
                vacuum.backtrack_movement()
            vacuum.turn_left()
        return False

    return explore(0)