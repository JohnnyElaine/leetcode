#!/usr/bin/env python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''

        for i in range(len(s)):
            # early exit:
            # remaining palindromes cannot be expanded to a larger size then current longest known palindrome
            # this means, the longest palindrome must have already been found
            if (len(s) - i) * 2 < len(longest_palindrome):
                return longest_palindrome

            # odd number of letters
            left, right = self.expandPalindrome(i, i, s)

            if right - left + 1 > len(longest_palindrome):
                longest_palindrome = s[left: right + 1]

            # even number of letters
            left, right = self.expandPalindrome(i, i + 1, s)

            if right - left + 1 > len(longest_palindrome):
                longest_palindrome = s[left: right + 1]

        return longest_palindrome

    def expandPalindrome(self, start_index_left: int, start_index_right: int, s: str) -> str:
        """
        Given two adjacent starting indicies within the string s, expand the string in both directions to find the longest palindrome.
        """
        left = start_index_left
        right = start_index_right

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

