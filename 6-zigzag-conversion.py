#!/usr/bin/env python
# TODO: find more efficient solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        numCols = 0

        if len(s) % 2 == 0:
            numCols = len(s) // 2
        else:
            numCols = len(s) // 2 + 1

        # row-major grid
        grid = [''] * (numRows * numCols)

        row = 0
        col = 0

        row_dir = 1
        col_dir = 0

        for c in s:
            grid[row * numCols + col] = c

            if row == numRows -1:
                row_dir = -1
                col_dir = 1

            elif row == 0:
                row_dir = 1
                col_dir = 0
            
            row += row_dir
            col += col_dir

        res = ''

        for row in range(numRows):
            for col in range(numCols):
                res += grid[row * numCols + col]
        
        return res
        

s = Solution()

print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 4))
print(s.convert('A', 1))