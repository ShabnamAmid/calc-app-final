"""A simple calculator supporting the four basic arithmetic operations."""


def calculate(first, second, operation):
    """Calculate the result of an arithmetic operation.

    Args:
        first: The first numeric operand.
        second: The second numeric operand.
        operation: One of '+', '-', '*', or '/'.

    Raises:
        ValueError: If the operation is not supported.
        ZeroDivisionError: If division by zero is attempted.
    """
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
