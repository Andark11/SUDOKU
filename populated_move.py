from typing import List, Tuple
from copy import deepcopy

def populate_board_with_possible_move(
    board: List[List[int]], posibles_moves: List[List[List[int]]]
) -> Tuple[List[List[int]], List[List[List[int]]], bool]:
    board_copy = deepcopy(board)
    posibles_moves_copy = deepcopy(posibles_moves)

    for row_index, row in enumerate(posibles_moves):
        for column_index, column in enumerate(row):
            if len(column) != 1:
                continue
            board_copy[row_index][column_index] = column[0]
            posibles_moves_copy[row_index][column_index] = []
            return board_copy, posibles_moves_copy, True
    
    return board_copy, posibles_moves_copy, False
