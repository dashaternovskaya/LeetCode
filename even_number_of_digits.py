

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            digits_counter = 1
            while len(str(num)) > 1:
                num //= 10
                digits_counter += 1
            if digits_counter % 2 == 0:
                answer += 1
        return answer
