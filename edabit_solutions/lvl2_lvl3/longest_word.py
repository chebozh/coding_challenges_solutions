"""Find the Longest Word

Write a function that will return the longest word in a sentence. In cases where more than one word is found,
return the first one.
Examples

find_longest("A thing of beauty is a joy forever.") ➞ "forever"

find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"

find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

Notes

    Special characters and symbols don't count as part of the word.
    Return the longest word found in lowercase letters."""

import re


def find_longest(sentence):
    words = [re.sub(r'\'\w+|"', '', word) for word in sentence[:-1].split(' ')]
    longest = max(words, key=lambda x: (len(x), words.index(x) * -1))
    return longest.lower()

if __name__ == '__main__':
    assert find_longest("A thing of beauty is a joy forever.") == "forever"

    assert find_longest("Forgetfulness is by all means powerless!") == "forgetfulness"

    assert find_longest(
        "\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") == "strengths"