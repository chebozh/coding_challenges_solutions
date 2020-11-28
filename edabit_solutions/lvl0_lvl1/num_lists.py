"""Create a function that takes four lists as arguments and returns a count of
the total number of identical lists.

Examples

count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]) ➞ 2

count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]) ➞ 0

count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]) ➞ 3
"""


def count_identical_lists(lst1, lst2, lst3, lst4):
    lists = [lst1, lst2, lst3, lst4]
    return len([sublist for sublist in lists if lists.count(sublist) > 1])


if __name__ == '__main__':
    assert count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]) == 2

    assert count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]) == 0

    assert count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]) == 3
