"""
Paul Cipher

In Paul Cipher, only alpha characters will be encoded with the following rules:

    All alpha characters will be treated as uppercase letters.
    The first alpha character will not change (except for switching to upper case).
    All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha
    character (wrap back to "A" if "Z" is passed).

he1lo would be encoded as follows:

paul_cipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)

Given a string txt, return the encoded message. See the below examples for a better understanding:
Examples

paul_cipher("muBas41r") ➞ "MHWCT41K"

paul_cipher("a1rForce") ➞ "A1SXUGUH"

paul_cipher("MATT") ➞ "MNUN"
"""


def paul_cipher(txt):
    res, prev = [], 0

    for ch in txt.upper():
        if ch.isalpha() and prev:
            curr = ord(ch) - 64
            new_ch = chr(((prev + curr) % 26) + 64)
            res.append(new_ch)
            prev = curr
        elif ch.isalpha() and not prev:
            res.append(ch)
            prev = ord(ch) - 64
        else:
            res.append(ch)

    return ''.join(res)


if __name__ == '__main__':
    assert paul_cipher("muBas41r") == "MHWCT41K"

    assert paul_cipher("a1rForce") == "A1SXUGUH"

    assert paul_cipher("MATT") == "MNUN"

    assert paul_cipher("4elen10ve") == "4EQQS10JA"
