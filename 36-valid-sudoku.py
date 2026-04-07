#!/usr/bin/env python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ZERO = ord('0')

        GRID_SIZE = 9
        BOX_SIZE = 3
        NUM_POSSIBLE_VALUES_PER_CELL = 10

        cols = [[False] * NUM_POSSIBLE_VALUES_PER_CELL for _ in range(GRID_SIZE)]
        boxes = [[False] * NUM_POSSIBLE_VALUES_PER_CELL for _ in range(GRID_SIZE)]

        for row_i in range(GRID_SIZE):
            # doesnt need to be pre-allocated for every row --> we can just reset it every loop iteration
            # this is somehow cheaper in python, since we avoid the dreaded 2D array access
            row = [False] * NUM_POSSIBLE_VALUES_PER_CELL
            for col_i in range(GRID_SIZE):
                elem = board[row_i][col_i]
                if elem == '.':
                    continue

                # convert elem to int, so we can use it as index in primitive set (i.e. an array)
                idx = ord(elem) - ZERO

                # flatten boxes 2D -> 1D
                box_idx = row_i // BOX_SIZE * BOX_SIZE + col_i // BOX_SIZE

                # check if value is unique in this row/col/box
                if row[idx] or cols[col_i][idx] or boxes[box_idx][idx]:
                    return False

                row[idx] = True
                cols[col_i][idx] = True
                boxes[box_idx][idx] = True

        return True



s = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","GRID_SIZE","5",".",".","."]
,[".","GRID_SIZE","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","GRID_SIZE",".",".","5"]
,[".",".",".",".","8",".",".","7","GRID_SIZE"]]

print(s.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","GRID_SIZE","5",".",".","."]
,[".","GRID_SIZE","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","GRID_SIZE",".",".","5"]
,[".",".",".",".","8",".",".","7","GRID_SIZE"]]

print(s.isValidSudoku(board))
