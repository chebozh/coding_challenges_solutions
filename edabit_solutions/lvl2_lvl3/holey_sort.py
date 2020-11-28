"""Holey Sort

https://edabit.com/challenge/fsNMnyjMkErQtvpMW

What do the numbers 4, 6, 8, 9 and 0 have in common? They all have holes in them! Notice how the number 8 contains not
one, but two holes.

Given a list of numbers, sort the list in accordance to how many holes occur in the number. It should be sorted in
ascending order.
Examples

holey_sort([44, 4, 444, 4444]) ➞ [4, 44, 444, 4444]

holey_sort([100, 888, 1660, 11]) ➞ [11, 100, 1660, 888]

holey_sort([8, 121, 41, 66]) ➞ [121, 41, 8, 66]

Notes

If two numbers have the same number of holes in them, sort them by the order they first appeared in.
Despite the number 0 appearing to have two holes in certain fonts, it will only have one hole for the purposes of this
challenge.
"""


# solution
def holey_sort(lst):
    letter_holes = {
        '0': 1,
        '4': 1,
        '6': 1,
        '8': 2,
        '9': 1,
    }
    holes_score = lambda x: sum(letter_holes.get(ch, 0) for ch in x)
    lst_str = (str(n) for n in lst)
    return list(map(int, sorted(lst_str, key=holes_score)))


if __name__ == '__main__':
    assert holey_sort([44, 4, 444, 4444]) == [4, 44, 444, 4444]

    assert holey_sort([100, 888, 1660, 11]) == [11, 100, 1660, 888]

    assert holey_sort([8, 121, 41, 66]) == [121, 41, 8, 66]
