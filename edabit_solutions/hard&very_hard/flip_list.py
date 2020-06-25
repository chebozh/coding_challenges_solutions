"""Flip the Array

Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.

In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column),
 and vice versa.

Examples

flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.

flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# Take a vertical list and flip it horizontal.

flip_list([]) ➞ []

Notes

If given an empty list [], return an empty list [].
"""


# solution
def flip_list(lst):
    if not lst:
        return lst
    elif all(isinstance(e, int) for e in lst):
        return [[e] for e in lst]
    else:
        return [e[0] for e in lst]


if __name__ == '__main__':
    assert flip_list([1, 2, 3, 4]) == [[1], [2], [3], [4]]

    assert flip_list([[5], [6], [9]]) == [5, 6, 9]

    assert flip_list([]) == []
