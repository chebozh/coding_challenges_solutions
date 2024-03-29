"""Difference Cipher

It's time to send and receive secret messages.

Create a single function that takes a string or a list and returns a coded or decoded message.

The first letter of the string, or the first element of the list represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.
Examples

dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
# H = 72, the difference between the H and e is 29 (upper- and lowercase).
# The difference between the two l's is obviously 0.

dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]

Notes

The input of the function will always be a string or a list with numbers."""


def diff_ciph(inpt):
    if isinstance(inpt, str):
        return encode(inpt)
    elif isinstance(inpt, list):
        return decode(inpt)


def encode(inpt):
    res = [ord(inpt[0])]
    for i in range(1, len(inpt)):
        res.append(ord(inpt[i]) - ord(inpt[i - 1]))
    return res


def decode(inpt):
    ch = inpt[0]
    res = [chr(ch)]
    for i in range(1, len(inpt)):
        ch += inpt[i]
        res.append(chr(ch))
    return ''.join(ch for ch in res)


if __name__ == '__main__':
    assert diff_ciph("Hello") == [72, 29, 7, 0, 3]
    assert diff_ciph("Sunshine") == [83, 34, -7, 5, -11, 1, 5, -9]
    assert diff_ciph([72, 33, -73, 84, -12, -3, 13, -13, -68]) == "Hi there!"
