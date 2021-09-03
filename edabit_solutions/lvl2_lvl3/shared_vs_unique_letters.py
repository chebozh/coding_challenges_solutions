"""
Shared vs. Unique Letters

Create a function that takes in two words as input and returns a list of three elements, in the following order:

    Shared letters between two words.
    Letters unique to word 1.
    Letters unique to word 2.

Each element should have unique letters, and have each letter be alphabetically sorted.
Examples

letters("sharp", "soap") ➞ ["aps", "hr", "o"]

letters("board", "bored") ➞ ["bdor", "a", "e"]

letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]

letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should
# only exist a single "f" in your first element.

letters("match", "ham") ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already
# in "match".

Notes

    Both words will be in lower case.
    You do not have to worry about punctuation, all words only have letters from [a-z].
    If an element contains no letters, return an empty string (see last example).
"""


def letters(word1, word2):
    shared_letters = ''.join(sorted(set(ch for ch in word1 if ch in word2)))
    word1_letters = ''.join(sorted(set(ch for ch in word1 if ch not in word2)))
    word2_letters = ''.join(sorted(set(ch for ch in word2 if ch not in word1)))
    return [shared_letters, word1_letters, word2_letters]

if __name__ == '__main__':
    assert letters("sharp", "soap") == ["aps", "hr", "o"]

    assert letters("board", "bored") == ["bdor", "a", "e"]

    assert letters("happiness", "envelope") == ["enp", "ahis", "lov"]

    assert letters("kerfuffle", "fluffy") == ["flu", "ekr", "y"]
    # Even with multiple matching letters (e.g. 3 f's), there should
    # only exist a single "f" in your first element.

    assert letters("match", "ham") == ["ahm", "ct", ""]
    # "ham" does not contain any letters that are not found already
    # in "match".