"""Boolean Chain

Write three functions:

    boolean_and
    boolean_or
    boolean_xor

These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating
pairwise.

Examples

boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False

boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True

boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False

Notes

    XOR is the same as OR, except that it excludes [True, True].
    Each time you evaluate an element at 0 and at 1, you collapse it into the single result."""

from functools import reduce


def boolean_and(lst):
    return reduce(lambda x, y: x and y, lst)


def boolean_or(lst):
    return reduce(lambda x, y: x or y, lst)


def boolean_xor(lst):
    return reduce(lambda x, y: x ^ y, lst)


if __name__ == '__main__':
    assert boolean_and([True, True, False, True]) is False

    assert boolean_or([True, True, False, False]) is True

    assert boolean_xor([True, True, False, False]) is False
