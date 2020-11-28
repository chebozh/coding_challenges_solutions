"""Product of Digits of Sum

https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb

Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the
answer is only 1 digit long.

Examples

sum_dig_prod(16, 28) ➞ 6

sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2

Notes

The input of the function is at least one number.
"""

# solution
from functools import reduce


def sum_dig_prod(*args):
    s = map(int, str(sum(args)))
    p = reduce(lambda x, y: x * y, s)
    return p if p <= 9 else sum_dig_prod(p)


if __name__ == '__main__':
    assert sum_dig_prod(16, 28) == 6

    assert sum_dig_prod(0) == 0

    assert sum_dig_prod(1, 2, 3, 4, 5, 6) == 2
