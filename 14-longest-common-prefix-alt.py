#!/usr/bin/env python
class Solution:
    """
    original solution using horizontal scanning.
    assumes the first word as the prefix and then shrinks with each visited word.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        if strs[0] == '':
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            if len(word) == 0:
                return ''
            if len(prefix) > len(word):
                prefix = prefix[:len(word)]
            for j in range(len(prefix)):
                if prefix[j] != word[j]:
                    prefix = prefix[:j]
                    break

        return prefix
