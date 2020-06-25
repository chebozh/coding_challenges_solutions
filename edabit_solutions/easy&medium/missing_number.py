"""Find the Missing Number

Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

Examples

missing_nums([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_nums([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_nums([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7

Notes

The list of numbers will be unsorted (not in order).
Only one number will be missing.
"""


# solution
def missing_nums(lst):
    for n in range(1, 11):
        if n not in lst:
            return n


if __name__ == '__main__':
    assert missing_nums([1, 2, 3, 4, 6, 7, 8, 9, 10]) == 5

    assert missing_nums([7, 2, 3, 6, 5, 9, 1, 4, 8]) == 10

    assert missing_nums([10, 5, 1, 2, 4, 6, 8, 3, 9]) == 7
