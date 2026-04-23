from TP1classes import Vacuum

def solve_maze_iterative(vacuum, max_depth):
    visited = set()
    path_stack = []
    
    path_stack.append((vacuum.row, vacuum.col, vacuum.direction, 0)) # (row, col, entry_direction, current_depth)
    visited.add((vacuum.row, vacuum.col))

    while path_stack:
        curr_row, curr_col, curr_dir, curr_depth = path_stack[-1]
        moved_this_turn = False

        if curr_depth < max_depth:
            for _ in range(4):
                front_cell = vacuum.see()
                
                if front_cell == 'E':
                    vacuum.move_forward()
                    return True
                
                increments_row, increments_col = Vacuum.DIR_OPS[vacuum.direction]
                next_row, next_col = vacuum.row + increments_row, vacuum.col + increments_col
                
                if front_cell in ('O', 'S') and (next_row, next_col) not in visited:
                    vacuum.move_forward()
                    visited.add((next_row, next_col))
                    path_stack.append((next_row, next_col, vacuum.direction, curr_depth + 1))
                    moved_this_turn = True
                    break
                vacuum.turn_left()

        if not moved_this_turn:
            popped_r, popped_c, entry_dir, _ = path_stack.pop()
            if path_stack:
                while vacuum.direction != entry_dir:
                    vacuum.turn_left()
                vacuum.backtrack_movement()

    return False