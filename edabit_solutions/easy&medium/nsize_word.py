"""N-Sized Parts

Create a function that divides a string into parts of size n.
Examples

partition("chew", 2) ➞ ["ch", "ew"]

partition("thematic", 4) ➞ ["them", "atic"]

partition("c++", 2) ➞ ["c+", "+"]

Notes

For inputs that do not split evenly into N-sized parts, the last element in the array will have a "leftover" string
(see example #3).
"""

# solution
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def partition(txt, n):
    return [''.join(group) for group in grouper(txt, n, '')]


if __name__ == '__main__':
    assert partition("chew", 2) == ["ch", "ew"]
    assert partition("thematic", 4) == ["them", "atic"]
    assert partition("c++", 2) == ["c+", "+"]
    assert partition("movement", 2) == ["mo", "ve", "me", "nt"]
