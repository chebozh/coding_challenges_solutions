"""All Subsets that Add to a Value

Create a function that returns all sublists in a list that sum to a particular value. Return the sublists in the
 following order:

    First by ascending length.
    Second by comparing element-by-element, starting from the leftmost one. Put the list with the smaller element
     first in the pairwise comparison.

The following example will illustrate:

get_subsets([-3, -2, -1, 0, 1, 2, 3], 2)
[ # All the subsets below sum to 2.
  [2],
  [-1, 3],
  [0, 2], # Same length: -1 < 0, so [-1, 3] goes before [0, 2]
  [-3, 2, 3],
  [-2, 1, 3],
  [-1, 0, 3],
  [-1, 1, 2],
  [-3, 0, 2, 3],
  [-2, -1, 2, 3],
  [-2, 0, 1, 3], # Same length + same first element: -1 < 0, so [-2, -1, 2, 3] goes before [-2, 0, 1, 3]
  [-1, 0, 1, 2],
  [-3, -1, 1, 2, 3],
  [-2, -1, 0, 2, 3],
  [-3, -1, 0, 1, 2, 3]
]

Examples

get_subsets([-1, 0, 1, 2], 2) ➞ [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]]

get_subsets([-1, 0, 1, 2], 3) ➞ [[1, 2], [0, 1, 2]]

get_subsets([1, 2, 3, 4], 5) ➞ [[1, 4], [2, 3]]

get_subsets([-1, 0, 1, 2], 4) ➞ []

Notes

    Lists will have unique numbers.
    Return an empty list if there does not a exist a subset whose numbers sum to that value (see fourth example)."""

from functools import cmp_to_key
from itertools import combinations


def get_subsets(lst, n):
    res = sub_lists(lst)
    res = [sl for sl in res if sum(sl) == n]
    res.sort(key=cmp_to_key(compare))
    res.sort(key=lambda sl: len(sl))
    return res


def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list) + 1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)
    return subs


def compare(sl1, sl2):
    for a, b in zip(sl1, sl2):
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0


if __name__ == '__main__':
    assert get_subsets([-1, 0, 1, 2], 2) == [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]]

    assert get_subsets([-1, 0, 1, 2], 3) == [[1, 2], [0, 1, 2]]

    assert get_subsets([1, 2, 3, 4], 5) == [[1, 4], [2, 3]]

    assert get_subsets([-1, 0, 1, 2], 4) == []
