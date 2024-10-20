def divide(a, b):
    return a / b


def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Делить на ноль нельзя")
    return dividend % divisor
