"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero_idx = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1
