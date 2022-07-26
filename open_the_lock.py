"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely
and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any
of these codes, the wheels of the lock will stop turning and you will be unable
to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1
if it is impossible.
"""

class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        queue = [0]
        visited = {0}
        steps = 0
        deadends_int = [int(x) for x in deadends]

        if 0 in deadends_int:
            return -1

        # BFS (Breadth-first Search) Algorithm:
        while queue:
            lenght = len(queue)
            for i in range(lenght):
                if queue[i] == int(target):
                    return steps
                else:
                    for n in (1, 10, 100, 1000):
                        # Check if there is digit 9 in number
                        if queue[i]%(n*10)//n == 9:
                            forward = queue[i]-9*n
                            backward = queue[i]-n
                        # Check if there is digit 0 in number
                        elif queue[i]%(n*10)//n == 0:
                            forward = queue[i]+n
                            backward = queue[i]+9*n
                        else:
                            forward = queue[i]+n
                            backward = queue[i]-n

                        for element in (forward, backward):
                            if element not in visited and element not in deadends_int:
                                queue.append(element)
                                visited.add(element)
            queue = queue[lenght:]
            steps += 1
        return -1
