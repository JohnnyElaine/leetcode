#!/usr/bin/env python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
            if carry == 0:
                break

        if carry > 0:
            digits.insert(0, 1)

        return digits
