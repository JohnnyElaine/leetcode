#!/usr/bin/env python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ZERO = ord('0')

        SUB_BOX_WIDTH = 3
        SUB_BOX_HEIGHT = 3

        num_rows = 9
        num_cols = 9

        # no list for rows needed, since we can clear the set each iteration of the outer for loop thats looping through the rows
        rows = [[False] * 10 for _ in range(num_rows)]
        cols = [[False] * 10 for _ in range(num_cols)]
        boxes = [[False] * 10 for _ in range(num_cols)]

        for row in range(num_rows):
            for col in range(num_cols):
                elem = board[row][col]
                if elem == '.':
                    continue

                # convert elem to int, so we can use it as index in primitive set (i.e. an array)
                idx = ord(elem) - ZERO

                box_idx = row // SUB_BOX_HEIGHT * SUB_BOX_WIDTH + col // SUB_BOX_WIDTH

                # check if value is unique in this row
                # check if value is unique in this column
                # check if value is uniqe in this sub box
                if rows[row][idx] or cols[col][idx] or boxes[box_idx][idx]:
                    return False

                rows[row][idx] = True
                cols[col][idx] = True
                boxes[box_idx][idx] = True

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
