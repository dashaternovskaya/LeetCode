"""
Given an array of integers arr, return True if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
a) arr.length >= 3
b) There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class Solution:
    def validMountainArray(self, arr: list) -> bool:
        # Finfing an index of the peak
        top_idx = arr.index(max(arr))

        if top_idx == 0 or top_idx == len(arr)-1 or len(arr) < 3:
            return False

        # Checking that elements to the left of the peak are strictly increasing
        for i in range(top_idx):
            if arr[i] >= arr[i+1] or arr[i] >= arr[top_idx]:
                return False

        # Checking that elements to the right of the peak are strictly decreasing
        for i in range(len(arr)-1, top_idx, -1):
            if arr[i-1] <= arr[i] or arr[i] >= arr[top_idx]:
                return False
        return True
