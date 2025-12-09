from typing import List

def posible_width_moves(board,y_position):
    all_moves = list(range(1,10))
    for column in board[y_position]:
        if column in all_moves:
            all_moves.remove(column)
    return all_moves

def posible_height_moves(board,x_position):
    all_moves = list(range(1,10))
    for row in board:
        if row[x_position] in all_moves:
            all_moves.remove(row[x_position])
    return all_moves

def posible_box_moves(board,box_row,box_column):
    all_moves = list(range(1,10))
    for row in range(box_row*3, box_row*3 + 3):
        for column in range(box_column*3, box_column*3 + 3):
            if board[row][column] in all_moves:
                all_moves.remove(board[row][column])
    return all_moves 

def get_tile_posibles_moves(
    board: List[List[int]], x_position: int, y_position: int
) -> List[int]:
    if board[y_position][x_position] != 0:
        return []

    return list(
        set(posible_width_moves(board=board,y_position=y_position))
        & set(posible_height_moves(board=board,x_position=x_position))
        & set(
            posible_box_moves(
                board=board,
                box_row=y_position // 3,
                box_column=x_position // 3,
            )
        )
    )

def get_board_posibles_moves(board: List[List[int]]) -> List[List[List[int]]]:
    prediction_board: List[List[List[int]]] = []
    for row_index, row in enumerate(board):
        prediction_board.append([])
        for column_index, _ in enumerate(row):
            prediction_board[row_index].append(
                get_tile_posibles_moves(
                    board=board, x_position=column_index, y_position=row_index
                )
            )
    return prediction_board