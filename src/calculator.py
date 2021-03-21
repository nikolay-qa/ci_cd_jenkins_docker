def add(a, b):
    check_inputs(a, b)
    return a + b


def subtract(a, b):
    check_inputs(a, b)
    return a - b


def multiply(a, b):
    check_inputs(a, b)
    return a * b


def divide(a, b):
    check_inputs(a, b)
    return a / b


def check_inputs(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be either int or float!")
