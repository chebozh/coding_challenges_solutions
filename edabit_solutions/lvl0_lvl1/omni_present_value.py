"""Omnipresent Value

A value is omnipresent if it exists in every sublist inside the main list.

To illustrate:

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
# 3 exists in every element inside this list, so is omnipresent.

Create a function that determines whether an input value is omnipresent for a given list.
"""


# solution
def is_omnipresent(lst, val):
    return all(val in sublist for sublist in lst)


if __name__ == '__main__':
    assert is_omnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]], 3) is True
    assert is_omnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]], 4) is False
