"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means
the expression would always evaluate to a result, and there will not be any division
by zero operation.
"""

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                r, l = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(l+r)
                elif token == '-':
                    stack.append(l-r)
                elif token == '*':
                    result = stack.append(l*r)
                else:
                    stack.append(int(l/r))
        return stack.pop()
