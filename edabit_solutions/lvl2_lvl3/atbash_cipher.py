"""Atbash Cipher

The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the
alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples

atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

Notes

    Capitalisation should be retained.
    Non-alphabetic characters should not be altered.
"""
import string


def atbash(txt):
    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    res = []

    for ch in txt:
        if ch.isalpha():
            opposite_idx = ((ascii_lowercase.index(ch) if ch.islower()
                             else ascii_uppercase.index(ch)) + 1) * -1

            opposite_letter = (ascii_lowercase[opposite_idx] if ch.islower()
                               else ascii_uppercase[opposite_idx])
            res.append(opposite_letter)
        else:
            res.append(ch)
    return ''.join(res)


if __name__ == '__main__':
    assert atbash("apple") == "zkkov"

    assert atbash("Hello world!") == "Svool dliow!"

    assert atbash("Christmas is the 25th of December") == "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
