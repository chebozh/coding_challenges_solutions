"""Fridge Poetry

Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another
phrase txt2.

Examples

can_build("got 2 go", "gogogo 2 today") ➞ True

can_build("sit on top", "its a moo point") ➞ True

can_build("long high add or", "highway road go long") ➞ False

can_build("fill tuck mid", "truck falls dim") ➞ False

Notes

    All letters will be in lower case.
    Numbers and special characters included.
    Ignore whitespaces.
    Do not count white space as a character.
"""


def can_build(txt1, txt2):
    return all(ch in txt2 and txt1.count(ch) <= txt2.count(ch)
               for ch in txt1
               if ch != ' ')


if __name__ == '__main__':
    assert can_build("got 2 go", "gogogo 2 today") is True

    assert can_build("sit on top", "its a moo point") is True

    assert can_build("long high add or", "highway road go long") is False

    assert can_build("fill tuck mid", "truck falls dim") is False
