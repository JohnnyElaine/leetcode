#!/usr/bin/env python
# TODO: find more efficient solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        rows = [''] * numRows

        row = 0

        row_direction = 1

        for c in s:
            rows[row] += c

            if row == numRows -1:
                row_direction = -1
            elif row == 0:
                row_direction = 1
            
            row += row_direction

        return "".join(rows)
        

s = Solution()

print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 4))
print(s.convert('A', 1))