"""Pentagonal Number

(https://edabit.com/challenge/st8mDxreMcuWxuz8c)

Write a function that takes a positive integer and calculates how many dots exist in a pentagonal shape around the
center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third,
there are 16 dots, and on the fourth there are 31 dots.

alt text

Return the number of dots that exist in the whole pentagon on the Nth iteration.

Examples

pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

pentagonal(3) ➞ 16

pentagonal(8) ➞ 141
"""


def pentagonal(num):
    return ((5 * num**2) - (5 * num) + 2) / 2


if __name__ == '__main__':
    assert pentagonal(1) == 1

    assert pentagonal(2) == 6

    assert pentagonal(3) == 16

    assert pentagonal(8) == 141
