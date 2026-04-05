#!/usr/bin/env python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue

            if i != k:
                nums[k] = nums[i]
            k += 1

        return k

    def removeElementBadSolution(self, nums: List[int], val: int) -> int:
        k = 0
        for target in range(len(nums)):
            if nums[target] != val:
                k += 1
                continue

            source = target + 1
            while source < len(nums):
                if nums[source] != val:
                    break
                source += 1

            if (source >= len(nums)):
                return k

            # swap source and target
            nums[target] = nums[source]
            nums[source] = val

            k += 1

        return k
