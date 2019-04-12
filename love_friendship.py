"""If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.
"""
# solution
from string import ascii_lowercase


def words_to_marks(s):
    letters = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
    letter_sum = 0
    for letter in s:
        letter_sum += letters[letter]
    return letter_sum


# examples
print(words_to_marks('attitude'))  # 100)
print(words_to_marks('friends'))  # 75)
print(words_to_marks('family'))  # 66)
print(words_to_marks('selfness'))  # 99)
print(words_to_marks('knowledge'))  # 96)
