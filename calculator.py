"""A simple calculator supporting basic arithmetic operations."""

import math


def calculate(first, second, operation):
    """Calculate the result of an arithmetic operation.

    Args:
        first: The first numeric operand, or the value for square root.
        second: The second numeric operand. It is ignored for square root.
        operation: One of '+', '-', '*', '/', 'sqrt', or '√'.

    Raises:
        ValueError: If the operation is not supported or the square root
            operand is negative.
        ZeroDivisionError: If division by zero is attempted.
    """
    if operation in ("sqrt", "√"):
        return math.sqrt(first)
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return first / second
    raise ValueError(f"unsupported operation: {operation}")
