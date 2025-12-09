from typing import List

def is_complete_board(board: List[List[int]]) -> bool:
    for row in board:
        for column in row:
            if column == 0:
                return False
    return True
