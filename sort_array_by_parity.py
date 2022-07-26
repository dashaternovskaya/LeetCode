"""
Given an integer array nums, move all the even integers at the beginning
of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        odd_idx = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[odd_idx] = nums[odd_idx], nums[i]
                odd_idx += 1

        return nums
