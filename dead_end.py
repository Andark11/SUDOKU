from typing import List

def is_valid_board(
    board: List[List[int]], posibles_moves: List[List[List[int]]]
) -> bool:
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if column != 0:
                continue
            if not posibles_moves[row_index][column_index]:
                return False
    return True