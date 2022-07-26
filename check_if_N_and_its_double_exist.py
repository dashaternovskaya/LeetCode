"""
Given an array arr of integers, check if there exists two integers N and M
such that N is the double of M ( i.e. N = 2 * M).
"""

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        hash_table = set()

        if len(arr) == 0:
            return False

        for i in range(len(arr)):
            if (arr[i] * 2 in hash_table) or (arr[i] % 2 == 0 and arr[i] // 2 in hash_table):
                    return True
            else:
                hash_table.add(arr[i])
        return False
