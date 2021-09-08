"""
Eight Sums Up

Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of
pairs (sorted ascendingly). See the following examples for more details.
Examples

sums_up([1, 2, 3, 4, 5]) ➞ {"pairs": [[3, 5]]}

sums_up([1, 2, 3, 7, 9]) ➞ {"pairs": [[1, 7]]}

sums_up([10, 9, 7, 2, 8]) ➞ {"pairs": []}

sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ {"pairs": [[2, 6], [3, 5], [1, 7]]}
# [6, 2] first to complete the cycle (to sum up to 8)
# [5, 3] follows
# [1, 7] lastly
# the pair that completes the cycle is always found on the left
# [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.

Notes

    Return a dictionary with the key "pairs" and a value of the array.
    Remember the idea of "completes the cycle first" when getting the sort order of the pairs.
    Only unique numbers are present in the array.
    Return an empty array if nothing sums up to eight.
"""


def sums_up(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 8:
                res.append([lst[i], lst[j], j])

    return {'pairs': [sorted([e[0], e[1]]) for e in sorted(res, key=lambda x: x[-1])]}


if __name__ == '__main__':
    assert sums_up([1, 2, 3, 4, 5]) == {"pairs": [[3, 5]]}

    assert sums_up([1, 2, 3, 7, 9]) == {"pairs": [[1, 7]]}

    assert sums_up([10, 9, 7, 2, 8]) == {"pairs": []}

    assert sums_up([1, 6, 5, 4, 8, 2, 3, 7]) == {"pairs": [[2, 6], [3, 5], [1, 7]]}

    assert sums_up([10, 9, 7, 1, 8, -2, -1, 2, 6]) == {"pairs": [[1, 7], [-2, 10], [-1, 9], [2, 6]]}
