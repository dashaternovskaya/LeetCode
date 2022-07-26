"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter = 0
        answer = 0

        for num in nums:
            if num == 1:
                counter += 1
            else:
                answer = counter if answer < counter else answer
                counter = 0
        return max(counter, answer)
