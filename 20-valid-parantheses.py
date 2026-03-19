#!/usr/bin/env python
class Solution:
    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c in self.parentheses:
                stack.append(self.parentheses[c])
            elif len(stack) <= 0:
                return False
            elif c != stack.pop():
                return False
        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid("([)]"))

