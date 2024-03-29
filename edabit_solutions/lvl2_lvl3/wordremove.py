"""
Remove The Word!

Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples

remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

Notes

    If number of times a letter appears in the list is greater than the number of times the letter appears in the string,
    the extra letters should be left behind (see example #2).
    If all the letters in the list are used in the string, the function should return an empty list (see example #3).
"""


def remove_letters(letters, word):
    res = [l for l in letters if l not in word or letters.count(l) > word.count(l)]
    return sorted(set(res), key=res.index)


if __name__ == '__main__':
    assert remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") == ["w"]

    assert remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") == ["b", "g", "w"]

    assert remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") == []
