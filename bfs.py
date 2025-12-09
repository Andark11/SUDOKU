from typing import List, Tuple, Deque
from copy import deepcopy
from collections import deque
from posibles_movimientos import get_board_posibles_moves
from populated_move import populate_board_with_possible_move
from dead_end import is_valid_board
from is_complete_board import is_complete_board
from populated_move_smart import populate_board_with_possible_move_smart

def breadth_first_search(board: List[List[int]]) -> Tuple[List[List[int]], bool]:
    board_copy = deepcopy(board)
    possible_moves = get_board_posibles_moves(board=board_copy)
    
    # Cola para BFS: cada elemento es (board, possible_moves)
    queue: Deque[Tuple[List[List[int]], List[List[List[int]]]]] = deque()
    queue.append((board_copy, possible_moves))
    
    while queue:
        current_board, current_moves = queue.popleft()
        
        # Intentar llenar el tablero con movimientos obvios
        update_occured = True
        while update_occured and not is_complete_board(board=current_board):
            current_board, current_moves, update_occured = populate_board_with_possible_move(
                board=current_board, posibles_moves=current_moves
            )
            
            if update_occured:
                current_moves = get_board_posibles_moves(board=current_board)
                continue
            
            current_board, current_moves, update_occured = populate_board_with_possible_move_smart(
                board=current_board, posibles_moves=current_moves
            )
            
            if update_occured:
                current_moves = get_board_posibles_moves(board=current_board)
        
        # Si está completo, hemos terminado
        if is_complete_board(board=current_board):
            return current_board, True
        
        # Si no es válido, descartar este estado
        if not is_valid_board(board=current_board, posibles_moves=current_moves):
            continue
        
        # Encontrar la primera celda con múltiples opciones
        found = False
        for row_index, row in enumerate(current_moves):
            if found:
                break
            for column_index, column in enumerate(row):
                if len(column) >= 2:
                    # Crear un nuevo estado para cada posible movimiento
                    for guess_move in column:
                        new_board = deepcopy(current_board)
                        new_board[row_index][column_index] = guess_move
                        new_moves = get_board_posibles_moves(board=new_board)
                        
                        # Agregar a la cola si es válido
                        if is_valid_board(board=new_board, posibles_moves=new_moves):
                            queue.append((new_board, new_moves))
                    
                    found = True
                    break
    
    return board, False
