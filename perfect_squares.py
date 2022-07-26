"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself. For example, 1, 4, 9, and 16
are perfect squares while 3 and 11 are not.
"""

class Solution:

    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        steps, parents, children = 1, {n}, set()

        # BFS (Breadth-first Search) Algorithm:
        while parents:
            for node in parents:
                for square in squares:
                    if node == square:
                        return steps
                    if node < square:
                        break
                    children.add(node-square)
            parents, children, steps = children, set(), steps+1
