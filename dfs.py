from typing import List, Tuple
from copy import deepcopy
import time
from posibles_movimientos import get_board_posibles_moves
from populated_move import populate_board_with_possible_move
from dead_end import is_valid_board
from is_complete_board import is_complete_board
from populated_move_smart import populate_board_with_possible_move_smart

def depth_first_search(board: List[List[int]]) -> Tuple[List[List[int]], bool]:
    board_copy = deepcopy(board)
    possible_moves = get_board_posibles_moves(board=board_copy)
    update_occured = True
    move_history: List[Tuple[List[List[int]], List[List[List[int]]]]] = []
    
    while not is_complete_board(board=board_copy):
        board_copy, possible_moves, update_occured = populate_board_with_possible_move(
            board=board_copy, posibles_moves=possible_moves
        )
        
        if update_occured:
            possible_moves = get_board_posibles_moves(board=board_copy)
            continue
        
        (board_copy, possible_moves, update_occured,) = populate_board_with_possible_move_smart(
            board=board_copy, posibles_moves=possible_moves
        )
        
        if update_occured:
            possible_moves = get_board_posibles_moves(board=board_copy)
            continue
        
        time.sleep(0.1)
        
        if (not is_valid_board(board=board_copy, posibles_moves=possible_moves)
            and not move_history):
            return board, False
        
        if not is_valid_board(board=board_copy, posibles_moves=possible_moves):
            board_copy = deepcopy(move_history[-1][0])
            possible_moves = deepcopy(move_history[-1][1])
            del move_history[-1]
            continue
        
        # Part 2: DFS
        if not is_valid_board(board=board_copy, posibles_moves=possible_moves):
            board_copy = deepcopy(move_history[-1][0])
            possible_moves = deepcopy(move_history[-1][1])
            del move_history[-1]
            continue
        
        x_position = -1
        y_position = -1
        guess_move = -1
        early_exit = False
        
        for row_index, row in enumerate(possible_moves):
            for column_index, column in enumerate(row):
                if len(column) < 2:
                    continue
                y_position = row_index
                x_position = column_index
                guess_move = column[0]
                early_exit = True
                break
            if early_exit:
                break
        
        possible_moves[y_position][x_position].remove(guess_move)
        move_history.append((deepcopy(board_copy), deepcopy(possible_moves)))
        board_copy[y_position][x_position] = guess_move
        possible_moves = get_board_posibles_moves(board=board_copy)
    
    return board_copy, True