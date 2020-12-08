"""
Next Prime

Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
Examples

next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
"""

import sys


def next_prime(num):
    if is_prime(num):
        return num
    for n in range(num, sys.maxsize):
        if is_prime(n):
            return n


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    assert next_prime(12) == 13

    assert next_prime(24) == 29

    assert next_prime(11) == 11
