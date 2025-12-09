from typing import List
import time
import random
from copy import deepcopy
from dfs import depth_first_search
from bfs import breadth_first_search
from genetic_algorithm import genetic_algorithm

def print_board(board: List[List[int]]) -> None:
    """Imprime el tablero de Sudoku de forma visual"""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print()

def is_valid_move(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """Verifica si un número es válido en una posición"""
    # Verificar fila
    if num in board[row]:
        return False
    
    # Verificar columna
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Verificar caja 3x3
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def fill_board(board: List[List[int]]) -> bool:
    """Llena el tablero completamente con una solución válida"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_sudoku(difficulty: str) -> List[List[int]]:
    """Genera un Sudoku aleatorio según el nivel de dificultad"""
    # Crear tablero vacío
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Llenar el tablero completamente
    fill_board(board)
    
    # Determinar cuántas celdas remover según dificultad
    cells_to_remove = {
        'facil': 30,
        'medio': 40,
        'dificil': 50,
        'extremo': 60
    }
    
    remove_count = cells_to_remove.get(difficulty, 40)
    
    # Remover celdas aleatoriamente
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    
    for i in range(remove_count):
        row, col = positions[i]
        board[row][col] = 0
    
    return board

def main():
    while True:
        print("\n" + "="*50)
        print("=== SOLUCIONADOR DE SUDOKU ===")
        print("="*50 + "\n")
        
        # Seleccionar algoritmo
        print("Seleccione el algoritmo:")
        print("1. DFS (Depth-First Search - Búsqueda en Profundidad)")
        print("2. BFS (Breadth-First Search - Búsqueda en Anchura)")
        print("3. GA (Genetic Algorithm - Algoritmo Genético)")
        
        while True:
            algo_choice = input("\nIngrese su opción (1-3): ").strip()
            if algo_choice in ['1', '2', '3']:
                algorithm_map = {'1': 'dfs', '2': 'bfs', '3': 'ga'}
                algorithm = algorithm_map[algo_choice]
                break
            else:
                print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
        
        # Seleccionar dificultad
        print("\nSeleccione el nivel de dificultad:")
        print("1. Fácil (30 celdas vacías)")
        print("2. Medio (40 celdas vacías)")
        print("3. Difícil (50 celdas vacías)")
        print("4. Extremo (60 celdas vacías)")
        
        while True:
            choice = input("\nIngrese su opción (1-4): ").strip()
            difficulty_map = {
                '1': 'facil',
                '2': 'medio',
                '3': 'dificil',
                '4': 'extremo'
            }
            
            if choice in difficulty_map:
                difficulty = difficulty_map[choice]
                break
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
        
        print(f"\nGenerando Sudoku nivel {difficulty}...\n")
        board = generate_sudoku(difficulty)
        
        print("Tablero inicial:")
        print_board(board)
        print(f"\nResolviendo con {algorithm.upper()}...\n")
        
        start_time = time.time()
        if algorithm == 'dfs':
            solved_board, success = depth_first_search(board)
        elif algorithm == 'bfs':
            solved_board, success = breadth_first_search(board)
        else:  # ga
            solved_board, success = genetic_algorithm(board)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if success:
            print("¡Sudoku resuelto!")
            print_board(solved_board)
            print(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos")
        else:
            print("No se pudo resolver el Sudoku")
            print_board(solved_board)
            print(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos")
        
        # Preguntar si quiere continuar
        print("\n" + "-"*50)
        while True:
            continue_choice = input("\n¿Desea resolver otro Sudoku? (s/n): ").strip().lower()
            if continue_choice in ['s', 'si', 'sí', 'y', 'yes']:
                break
            elif continue_choice in ['n', 'no']:
                print("\n¡Gracias por usar el Solucionador de Sudoku!")
                return
            else:
                print("Opción inválida. Por favor, ingrese 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()
