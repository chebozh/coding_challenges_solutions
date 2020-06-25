"""
Write a function that returns the total number of integers covered from a list of intervals (inclusive).

Examples

covered_integers([[80, 81], [1, 2], [9, 11]]) ➞ 7
# 7 Integers are covered: 1, 2, 9, 10, 11, 80, 81

covered_integers([[3, 6], [4, 6], [5, 6]]) ➞ 4

"""


def covered_integers(lst):
    res = []
    for pair in lst:
        res.extend([n for n in range(pair[0], pair[-1] + 1)])
    return len(set(res))


if __name__ == '__main__':
    assert covered_integers([[80, 81], [1, 2], [9, 11]]) == 7
    assert covered_integers([[3, 6], [4, 6], [5, 6]]) == 4
