#!/usr/bin/env python
class Solution:
    INT_MAX = 2**31-1
    INT_MIN = -2**31

    def is_digit(self, c: str) -> bool:
        return '0' <= c <= '9'

    def char_to_int(self, c: str) -> int:
        # ord('0') = 48
        return (ord(c) - 48)

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        idx = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            idx = 1
        if s[0] == '+':
            idx = 1

        res = 0

        while idx < len(s) and self.is_digit(s[idx]):
            res *= 10
            res += self.char_to_int(s[idx])
            idx += 1

        res *= sign

        return max(self.INT_MIN, min(res, self.INT_MAX))
