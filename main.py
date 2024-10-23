def divide(a, b):
    return a / b


def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Делить на ноль нельзя")
    return dividend % divisor

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
