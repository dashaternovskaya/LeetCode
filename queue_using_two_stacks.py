"""
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

--------------------------------------------------------------------------
Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
--------------------------------------------------------------------------

Notes:

– You must use only standard operations of a stack, which means only push to top,
peek/pop from top, size, and is empty operations are valid.
– Depending on your language, the stack may not be supported natively. You may
simulate a stack using a list or deque (double-ended queue) as long as you use
only a stack's standard operations.
"""

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []


    def push(self, x: int) -> None:
        if not self.input_stack:
            self.front = x
        self.input_stack.append(x)


    def pop(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()


    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        return self.front

    def empty(self) -> bool:
        return self.input_stack == [] and self.output_stack == []
