import sys
import time
import random

from BacktrackingClasses import Maze, Vacuum
from BacktrackingIterative import solve_maze_iterative as solve_iterative
from BacktrackingRecursive import solve_maze_recursive as solve_recursive

def generate_maze(rows, cols, wall_probability=0.25):
    grid = [[Maze.VACIO for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        grid[r][0] = grid[r][cols-1] = Maze.PARED
    for c in range(cols):
        grid[0][c] = grid[rows-1][c] = Maze.PARED
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if random.random() < wall_probability:
                grid[r][c] = Maze.PARED
                
    start_r = random.randint(1, rows - 2)
    start_c = random.randint(1, cols - 2)
    grid[start_r][start_c] = Maze.ENTRADA
    
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top': grid[0][random.randint(1, cols-2)] = Maze.SALIDA
    elif edge == 'bottom': grid[rows-1][random.randint(1, cols-2)] = Maze.SALIDA
    elif edge == 'left': grid[random.randint(1, rows-2)][0] = Maze.SALIDA
    else: grid[random.randint(1, rows-2)][cols-1] = Maze.SALIDA
        
    return grid, start_r, start_c

def print_maze(grid):
    for row in grid:
        print(" ".join(row))

if __name__ == "__main__":
    n_rows = 15
    m_cols = 15
    wall_prob = 0.2

    if len(sys.argv) >= 3:
        try:
            n_rows = int(sys.argv[1])
            m_cols = int(sys.argv[2])
            if len(sys.argv) == 4:
                wall_prob = float(sys.argv[3])
        except ValueError:
            print("Error: Las dimensiones deben ser números enteros y la probabilidad un decimal.")
            print("Uso: python TP1_main.py <filas> <columnas> [probabilidad_paredes]")
            sys.exit(1)
    elif len(sys.argv) != 1:
        print("Uso: python TP1_main.py <filas> <columnas> [probabilidad_paredes]")
        sys.exit(1)

    total_cells = n_rows * m_cols
    
    sys.setrecursionlimit(max(1000, total_cells + 100))

    print(f"\nBACKTRACKING - Generando cuadrícula de {n_rows}x{m_cols} con {wall_prob*100:.0f}% de paredes")
    maze_grid, s_r, s_c = generate_maze(n_rows, m_cols, wall_probability=wall_prob)
    my_maze = Maze(maze_grid)

    if n_rows <= 30 and m_cols <= 30:
        print("\nLaberinto:")
        print_maze(maze_grid)
    else:
        print("\n[ El diseño del laberinto es demasiado grande para mostrarse en la consola, sólo se imprimirán de menos de 30 casillas de ancho u largo ]")

    # ---------------------------------------------------------
    # ITERATIVO
    # ---------------------------------------------------------
    print("\n" + "="*45)
    print(" 1. EJECUTANDO DFS ITERATIVO")
    print("="*45)
    
    vacuum_iter = Vacuum(my_maze, s_r, s_c, start_dir=0)
    
    start_time_iter = time.perf_counter()
    success_iter = solve_iterative(vacuum_iter, max_depth=total_cells)
    end_time_iter = time.perf_counter()
    
    time_iter_ms = (end_time_iter - start_time_iter) * 1000
    
    print(f"  Resultado      : {'ÉXITO (Salida Encontrada)' if success_iter else 'FALLÓ (Sin Salida Alcanzable)'}")
    print(f"  Ops Físicas    : {vacuum_iter.ops_count}")
    print(f"  Backtracks     : {vacuum_iter.backtrack_count} (Ramas Podadas)")
    print(f"  Tiempo CPU     : {time_iter_ms:.4f} ms")

    # ---------------------------------------------------------
    # RECURSIVA
    # ---------------------------------------------------------
    print("\n" + "="*45)
    print(" 2. EJECUTANDO DFS RECURSIVO")
    print("="*45)
    
    vacuum_rec = Vacuum(my_maze, s_r, s_c, start_dir=0)
    
    start_time_rec = time.perf_counter()
    success_rec = solve_recursive(vacuum_rec, max_depth=total_cells)
    end_time_rec = time.perf_counter()
    
    time_rec_ms = (end_time_rec - start_time_rec) * 1000
    
    print(f"  Resultado      : {'ÉXITO (Salida Encontrada)' if success_rec else 'FALLÓ (Sin Salida Alcanzable)'}")
    print(f"  Ops Físicas    : {vacuum_rec.ops_count}")
    print(f"  Backtracks     : {vacuum_rec.backtrack_count} (Ramas Podadas)")
    print(f"  Tiempo CPU     : {time_rec_ms:.4f} ms")

    # ---------------------------------------------------------
    # COMPARACIÓN
    # ---------------------------------------------------------
    print("\n" + "="*45)
    print(" RESUMEN DE COMPARACIÓN")
    print("="*45)
    
    logic_match = "Mismo Árbol de Búsqueda" if vacuum_iter.backtrack_count == vacuum_rec.backtrack_count else "Divergencia entre métodos"
    ops_diff = vacuum_iter.ops_count - vacuum_rec.ops_count
    
    print(f"  Validación Lógica: {logic_match}")
    print(f"  Costo Mecánico   : El método Iterativo realizó {ops_diff} ops físicas extra")
    print("\n")
