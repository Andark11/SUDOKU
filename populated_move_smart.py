from typing import List, Tuple
from copy import deepcopy

def populate_board_with_possible_move_smart(
    board: List[List[int]], posibles_moves: List[List[List[int]]]
) -> Tuple[List[List[int]], List[List[List[int]]], bool]:
    board_copy = deepcopy(board)
    posibles_moves_copy = deepcopy(posibles_moves)
    
    # Check rows
    for row_index, row in enumerate(posibles_moves):
        for num in range(1, 10):
            positions = []
            for column_index, column in enumerate(row):
                if num in column:
                    positions.append(column_index)
            if len(positions) == 1:
                board_copy[row_index][positions[0]] = num
                posibles_moves_copy[row_index][positions[0]] = []
                return board_copy, posibles_moves_copy, True
    
    # Check columns
    for column_index in range(9):
        for num in range(1, 10):
            positions = []
            for row_index in range(9):
                if num in posibles_moves[row_index][column_index]:
                    positions.append(row_index)
            if len(positions) == 1:
                board_copy[positions[0]][column_index] = num
                posibles_moves_copy[positions[0]][column_index] = []
                return board_copy, posibles_moves_copy, True
    
    # Check boxes
    for box_row in range(3):
        for box_column in range(3):
            for num in range(1, 10):
                positions = []
                for row in range(box_row * 3, box_row * 3 + 3):
                    for column in range(box_column * 3, box_column * 3 + 3):
                        if num in posibles_moves[row][column]:
                            positions.append((row, column))
                if len(positions) == 1:
                    board_copy[positions[0][0]][positions[0][1]] = num
                    posibles_moves_copy[positions[0][0]][positions[0][1]] = []
                    return board_copy, posibles_moves_copy, True
    
    return board_copy, posibles_moves_copy, False
