"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares_lst = [num**2 for num in sorted(nums, key=lambda x: abs(x))]
        return squares_lst
