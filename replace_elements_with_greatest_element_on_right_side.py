"""
Given an array arr, replace every element in that array with the greatest element
among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

class Solution:
    def replaceElements(self, arr: list) -> list:
        max_element = -1

        for i in range(len(arr)-1, -1, -1):
            arr[i], max_element = max_element, max(arr[i], max_element)
        return arr
