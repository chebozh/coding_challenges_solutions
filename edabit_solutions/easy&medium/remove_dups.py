"""Remove Duplicates from List

Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential
 order as the old list (minus duplicates).
Examples

removeDups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]

removeDups([1, 0, 1, 0]) ➞ [1, 0]

removeDups(['The', 'big', 'cat']) ➞ ['The', 'big', 'cat']

Notes

Test cases contain lists with both strings and numbers.
Case sensitive.
"""
# solution
from collections import OrderedDict


def remove_dups(lst):
    # using OrderedDict to preserve order
    return list(OrderedDict.fromkeys(lst))


if __name__ == '__main__':
    assert remove_dups(["John", "Taylor", "John"]) == ["John", "Taylor"]

    assert remove_dups([1, 0, 1, 0]) == [1, 0]

    assert remove_dups(['The', 'big', 'cat']) == ['The', 'big', 'cat']
