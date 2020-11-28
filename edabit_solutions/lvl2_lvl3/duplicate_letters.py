"""Given a common phrase, return False if any individual word in the phrase contains duplicate letters.
 Return True otherwise.

Examples

no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
"""


def no_duplicate_letters(phrase):
    words = phrase.split()
    return False if any(word.count(letter) >= 2 for word in words for letter in word) else True


if __name__ == '__main__':
    assert no_duplicate_letters("Fortune favours the bold.") is True

    assert no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") is True

    assert no_duplicate_letters("Look before you leap.") is False
    # Duplicate letters in "Look" and "before".

    assert no_duplicate_letters("An apple a day keeps the doctor away.") is False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".
