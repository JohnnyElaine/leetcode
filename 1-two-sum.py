#!/usr/bin/env python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = diff to target (i.e. target - nums[i]), value = index in nums array
        diff_index_map = {}

        for i in  range(len(nums)):
            diff = target - nums[i]
            if diff in diff_index_map:
                return [i, diff_index_map[diff]]

            diff_index_map[nums[i]] = i


        return None
