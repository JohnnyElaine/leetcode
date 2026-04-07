#!/usr/bin/env python
class SudokuSet:
    ascii_val_zero = ord('0')

    def __init__(self):
        self.arr = [False] * 10

    def clear(self):
        self.arr = [False] * 10

    def add(self, c: str):
        self.arr[ord(c) - self.ascii_val_zero] = True

    def contains(self, c: str):
        return self.arr[ord(c) - self.ascii_val_zero]

class Solution:
    # somehow still very slow, TODO: improve runtime
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SUB_BOX_WIDTH = 3
        SUB_BOX_HEIGHT = 3

        num_rows = len(board)
        num_cols = len(board[0])

        # no list for rows needed, since we can clear the set each iteration of the outer for loop thats looping through the rows
        seen_vals_row = SudokuSet()
        seen_vals_columns = [SudokuSet() for _ in range(num_cols)]
        seen_vals_sub_boxes = [[SudokuSet() for _ in range(SUB_BOX_WIDTH)] for _ in range(SUB_BOX_HEIGHT)]

        for row in range(num_rows):
            seen_vals_row.clear()
            for col in range(num_cols):
                val = board[row][col]
                if val == '.':
                    continue

                # check if value is unique in this row
                if seen_vals_row.contains(val):
                    return False

                # check if value is unique in this column
                if seen_vals_columns[col].contains(val):
                    return False

                # check if value is uniqe in this sub box:
                sub_box_row = row // SUB_BOX_HEIGHT
                sub_box_col = col // SUB_BOX_WIDTH
                if seen_vals_sub_boxes[sub_box_row][sub_box_col].contains(val):
                    return False

                seen_vals_row.add(val)
                seen_vals_columns[col].add(val)
                seen_vals_sub_boxes[sub_box_row][sub_box_col].add(val)

        return True



s = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))
