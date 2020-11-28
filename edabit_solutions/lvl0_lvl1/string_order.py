"""Is the String in Order?

Create a function that takes a string and returns True or False,
depending on whether the characters are in order or not.

Examples

is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True

Notes

You don't have to handle empty strings.
"""


# solution
def is_in_order(txt):
    return all(ord(txt[i]) <= ord(txt[i + 1]) for i in range(len(txt) - 1))


if __name__ == '__main__':
    assert is_in_order("abc") is True
    assert is_in_order("edabit") is False
    assert is_in_order("123") is True
    assert is_in_order("xyzz") is True
