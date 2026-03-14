#!/usr/bin/env python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        if x % 10 == 0: # there are no numbers with leading zeros
            return False


        x_reverse = 0
        x_tmp = x

        while x_tmp > 0:
            digit = x_tmp % 10
            x_tmp //= 10
            x_reverse = x_reverse * 10 + digit

        return x == x_reverse
