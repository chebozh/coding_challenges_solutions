"""
WordRank Scoring System

Create a function that takes a string of words and returns the highest scoring word.
Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3, etc.

Examples

word_rank("The quick brown fox.") ➞ "brown"

word_rank("Nancy is very pretty.") ➞ "pretty"

word_rank("Check back tomorrow, man!") ➞ "tomorrow"

word_rank("Wednesday is hump day.") ➞ "Wednesday"

Notes

    If two words score the same, return the word that appears first in the original string.
    The returned string should only contain alphabetic characters (a-z).
    Preserve case in the returned string (see 4th example above).
"""
import string


def word_rank(txt):
    words = "".join(ch for ch in txt
                    if ch not in string.punctuation
                    and not ch.isdigit()).split()
    scores = []

    for word in words:
        word_score = 0
        word_idx = words.index(word)
        for ch in word:
            if ch.islower():
                word_score += string.ascii_lowercase.index(ch) + 1
            else:
                word_score += string.ascii_uppercase.index(ch) + 1
        scores.append((word, word_idx, word_score))
    return max(scores, key=lambda x: (x[-1], x[1]))[0]


if __name__ == '__main__':
    assert word_rank("The quick brown fox.") == "brown"

    assert word_rank("Nancy is very pretty.") == "pretty"

    assert word_rank("Check back tomorrow, man!") == "tomorrow"

    assert word_rank("Wednesday is hump day.") == "Wednesday"

    assert word_rank("The clock within this blog and the clock on my laptop are 1 hour different from each other."), "different"
