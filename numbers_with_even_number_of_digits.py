"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
