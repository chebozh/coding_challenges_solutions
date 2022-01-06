"""Isomorphic Strings

Given two strings s and t, create a function to determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
Examples

is_isomorphic("egg", "add") ➞ True

is_isomorphic("aba", "baa") ➞ False

is_isomorphic("paper", "title") ➞ True
"""


def is_isomorphic(s, t):
    return all(s.count(ss) == t.count(tt) for ss, tt in zip(s, t))


if __name__ == '__main__':
    assert is_isomorphic("egg", "add") is True

    assert is_isomorphic("aba", "baa") is False

    assert is_isomorphic("paper", "title") is True
