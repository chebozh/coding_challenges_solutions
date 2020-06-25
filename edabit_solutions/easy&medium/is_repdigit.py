"""Is the Number a Repdigit

A repdigit is a positive number composed out of the same digit.

Create a function that takes an integer and returns whether it's a repdigit or not.
Examples

is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False

Notes

    The number 0 should return True (even though it's not a positive number).
    Check the Resources tab for more info on repdigits.
"""


# solution
def is_repdigit(num):
    num_str = str(num)
    return all(ch == num_str[0] for ch in num_str)


if __name__ == '__main__':
    assert is_repdigit(66) is True
    assert is_repdigit(0) is True
    assert is_repdigit(-11) is False
