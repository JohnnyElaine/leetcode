#!/usr/bin/env python
class Solution:
    """
    classic implementation using Vertical Scanning
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]

        for word_i in range(len(ref)):
            for list_i in range(1, len(strs)):
                if word_i >= len(strs[list_i]) or ref[word_i] != strs[list_i][word_i]:
                    return ref[:word_i]

        return ref
