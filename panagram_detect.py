"""
A pangram is a sentence that contains every single letter of the alphabet at least once.

For example, the sentence "The quick brown fox jumps over the lazy dog" IS A pangram, because it uses the letters A-Z at
least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.

Available here: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
"""
# solution
import string


def is_pangram(s):
    s = set(s.lower())
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    return True


# Example
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))
