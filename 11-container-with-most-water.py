#!/usr/bin/env python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        highest = max(height)

        max_water = 0

        # while condition:
        # we calculate the the maximum theoretical water area for the current width (right - left)
        # if max_water > maxium theoretical water area for current width
        # then we can stop the loop, since it is impossible to find a larger value than max_water
        # since we can only decrease the width
        while (right - left) * highest >= max_water:
            w = right - left
            h = min(height[left], height[right])
            water = w * h

            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
