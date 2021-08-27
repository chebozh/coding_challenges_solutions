"""
Add the Values of the Symbols in a Matrix

Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or
 takes something from the total score. Symbol values:

    # = 5
    O = 3
    X = 1
    ! = -1
    !! = -3
    !!! = -5

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be
(0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
"""


def check_score(s):
    total = 0
    symbol_score = {
        '#': 5,
        'O': 3,
        'X': 1,
        '!': -1,
        '!!': -3,
        '!!!': -5,
    }
    for sublist in s:
        total += sum(symbol_score[symbol] for symbol in sublist)
    return max(0, total)


if __name__ == '__main__':
    assert check_score([
        ["#", "!"],
        ["!!", "X"]
    ]) == 2

    assert check_score([
        ["!!!", "O", "!"],
        ["X", "#", "!!!"],
        ["!!", "X", "O"]
    ]) == 0

    assert check_score([
        ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
        ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
        ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
        ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
        ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
        ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
        ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
        ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
        ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
        ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
        ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
        ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
        ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
        ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
    ]) == 12
