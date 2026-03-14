#!/usr/bin/env python
class Solution:
    numerals = {
        'I' : 1, 'V': 5, 'X' : 10,
        'L' : 50, 'C' : 100, 'D' : 500,
        'M' : 1000
    }

    def romanToInt(self, s: str) -> int:
        sum = self.numerals[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            c = s[i]
            right_c = s[i+1]
            if self.numerals[c] < self.numerals[right_c]:
                sum -= self.numerals[c]
            else:
                sum += self.numerals[c]
        return sum
