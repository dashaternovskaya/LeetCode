"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; there are no extra
white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there will not
be input like 3a or 2[4].
"""

class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, k))
                curr_str = ''
                k = 0
            elif char == ']':
                last_str, last_k = stack.pop(-1)
                curr_str = last_str + last_k * curr_str
            else:
                curr_str += char

        return curr_str
