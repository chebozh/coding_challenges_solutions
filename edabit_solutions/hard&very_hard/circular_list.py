"""Is the List Circular?

Write a function that determines if a list is circular. A list is circular if its sublists can be reordered such that
each sublist's last element is equal to the next sublist's first element.

For example, the list [[1, 1, 1], [9, 2, 3, 4], [4, 1], [1, 2, 5, 7, 9]] is circular because we can re-arrange the
elements to create the following list:

[[9, 2, 3, 4], [4, 1], [1, 1, 1], [1, 2, 5, 7, 9]]

Examples

is_circular([[9, 8], [6, 9, 1], [8, 4, 2], [1, 9], [2, 1, 6]]) ➞ True
# Can be reordered: [[9, 8], [8, 4, 2], [2, 1, 6], [6, 9, 1], [1, 9]]

is_circular([[1, 1], [1, 2]]) ➞ False

is_circular([[2, 1], [1, 2]]) ➞ True

is_circular([[2, 1], [1, 2], [2, 1], [1, 3, 1], [1, 4, 4]]) ➞ False

Notes

    In a circular re-ordering, the last sublist's last element must be identical to the first sublist's first element.
    Sublists will contain at least one element.
"""
# solution

from itertools import permutations


def is_circular(lst):
    for p in tuple(permutations(lst, len(lst))):
        if all(p[i][0] == p[i-1][-1] for i in range(len(lst))):
            return True
    return False


if __name__ == '__main__':
    assert is_circular([[9, 8], [6, 9, 1], [8, 4, 2], [1, 9], [2, 1, 6]]) is True
    # Can be reordered: [[9, 8], [8, 4, 2], [2, 1, 6], [6, 9, 1], [1, 9]]

    assert is_circular([[1, 1], [1, 2]]) is False

    assert is_circular([[2, 1], [1, 2]]) is True

    assert is_circular([[2, 1], [1, 2], [2, 1], [1, 3, 1], [1, 4, 4]]) is False