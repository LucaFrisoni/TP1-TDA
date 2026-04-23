import time
import random
import csv
import os
import sys

sys.setrecursionlimit(600000)

from TP1classes import Maze, Vacuum
from TP1iterativeV2 import solve_maze_iterative
from TP1recursiveV2 import solve_maze_recursive

def generate_maze(rows, cols, wall_probability=0.25):
    grid = [['O' for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        grid[r][0] = grid[r][cols-1] = 'X'
    for c in range(cols):
        grid[0][c] = grid[rows-1][c] = 'X'
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if random.random() < wall_probability:
                grid[r][c] = 'X'
                
    start_r, start_c = rows // 2, cols // 2
    grid[start_r][start_c] = 'S'
    
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top': grid[0][random.randint(1, cols-2)] = 'E'
    elif edge == 'bottom': grid[rows-1][random.randint(1, cols-2)] = 'E'
    elif edge == 'left': grid[random.randint(1, rows-2)][0] = 'E'
    else: grid[random.randint(1, rows-2)][cols-1] = 'E'
        
    return grid, start_r, start_c

def is_maze_solvable(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_r, start_c)]
    visited.add((start_r, start_c))
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]
                if cell == 'E':
                    return True
                if cell in ('O', 'S') and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc))
    return False

def generate_validated_maze(rows, cols, wall_probability=0.25, require_solvable=True):
    attempts = 0
    while True:
        attempts += 1
        grid, s_r, s_c = generate_maze(rows, cols, wall_probability)
        if is_maze_solvable(grid, s_r, s_c) == require_solvable:
            state_str = "solvable" if require_solvable else "unsolvable"
            print(f"  [Generated validated {state_str} maze in {attempts} attempts]")
            return grid, s_r, s_c

if __name__ == "__main__":
    maze_sizes = [10, 20, 30, 40, 50, 60, 80, 100, 120, 150, 250, 300, 400, 500, 600, 750, 1000]
    # maze_sizes = [10, 20, 30, 40, 50, 60, 80, 100]
    depth_limits = [22500]
    # depth_limits = [10, 25, 50, 100, 200, 500, 1000]
    TEST_SOLVABLE_MAZES = True
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(script_dir, "benchmark_solvable.csv")
    print(f"Starting DLS benchmark... Data will be saved to: {csv_filename}")
    print("-" * 60)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Maze_Size_N", "Total_Cells", "Is_Fundamentally_Solvable", "Max_Depth_Limit", "Found_Exit", 
            "Iterative_Time_ms", "Recursive_Time_ms", 
            "Iterative_Ops", "Recursive_Ops", "Iterative_Backtracks", "Recursive_Backtracks"
        ])
        for size in maze_sizes:
            print(f"\nTesting {size}x{size} maze...")
            maze_grid, s_r, s_c = generate_validated_maze(size, size, wall_probability=0.2, require_solvable=TEST_SOLVABLE_MAZES)
            my_maze = Maze(maze_grid)
            total_cells = size * size
            for limit in depth_limits:
                # --- Iterative ---
                vacuum_iter = Vacuum(my_maze, s_r, s_c, start_dir=0)
                start_time_iter = time.perf_counter()
                success_iter = solve_maze_iterative(vacuum_iter, max_depth=limit)
                end_time_iter = time.perf_counter()
                time_iter_ms = (end_time_iter - start_time_iter) * 1000
                # --- Recursive ---
                vacuum_rec = Vacuum(my_maze, s_r, s_c, start_dir=0)
                start_time_rec = time.perf_counter()
                success_rec = solve_maze_recursive(vacuum_rec, max_depth=limit)
                end_time_rec = time.perf_counter()
                time_rec_ms = (end_time_rec - start_time_rec) * 1000
                # --- Results Output ---
                writer.writerow([
                    size, total_cells, TEST_SOLVABLE_MAZES, limit, success_iter,
                    round(time_iter_ms, 4), round(time_rec_ms, 4),
                    vacuum_iter.ops_count, vacuum_rec.ops_count, vacuum_iter.backtrack_count, vacuum_rec.backtrack_count
                ])
                status = "SUCCESS" if success_iter else "FAILED"
                print(f"  -> Limit: {limit:3} | {status:7} | Ops (I/R): {vacuum_iter.ops_count:5} / {vacuum_rec.ops_count:5} | Backtracks (I/R): {vacuum_iter.backtrack_count:5} / {vacuum_rec.backtrack_count:5} | Time (I/R): {time_iter_ms:.4f} / {time_rec_ms:.4f} ms")
    print("-" * 60)
    print(f"Benchmarking complete. File saved to {csv_filename}")