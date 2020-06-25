"""Rhyme Time

Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise,
two lines rhyme if the last word from each sentence contains the same vowels.

Examples

does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True

does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.

does_rhyme("You are off to the races", "a splendid day.") ➞ False

does_rhyme("and frequently do?", "you gotta move.") ➞ False

Notes

Case insensitive.
Here we are disregarding cases like "thyme" and "lime".
We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different
vowels).
"""

# solution

import re


def does_rhyme(txt1, txt2):
    txt1_last = txt1.split()[-1][:-1].lower()
    txt2_last = txt2.split()[-1][:-1].lower()
    n = len(txt1_last) - 1
    pattern = f'.{ {n} }$'
    txt1_last_syllable = re.search(pattern, txt1_last).group()

    if txt1_last_syllable:
        if txt2_last.endswith(txt1_last_syllable):
            return True
        elif txt1_last_syllable[1:]:
            return txt2_last.endswith(txt1_last_syllable[1:])
    return False


if __name__ == '__main__':
    assert does_rhyme('your elbow and chin!', 'how much can you win?') is True

    assert does_rhyme("Sam I am!", "Green eggs and ham.") is True

    assert does_rhyme("Sam I am!", "Green eggs and HAM.") is True
    # Capitalization and punctuation should not matter.

    assert does_rhyme("You are off to the races", "a splendid day.") is False

    assert does_rhyme("and frequently do?", "you gotta move.") is False
