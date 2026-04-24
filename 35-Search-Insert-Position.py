#!/usr/bin/env python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            center = left + (right - left) // 2 
            if target > nums[center]:
                left = center + 1
            elif target < nums[center]:
                right = center - 1
            else:
                return center
        return left
