#!/usr/bin/env python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0

        left = 0

        for right in range(len(s)):
            right_c = s[right]
            if right_c in window:
                left_c = ""
                while left_c != right_c:
                    left_c = s[left]
                    window.remove(left_c)
                    left += 1

            window.add(right_c)

            max_len = max(right - left + 1, max_len)

        return max_len

s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
