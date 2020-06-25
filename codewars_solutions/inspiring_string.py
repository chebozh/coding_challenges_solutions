"""
When given a string of space separated words, return the word with the longest length. If there are multiple words with
the longest length, return the last instance of the word with the longest length.

Example:

'red white blue' //returns string value of white

'red blue gold' //returns gold

"""


# solution
def longest_word(string_of_words):
    list_of_strings = string_of_words.split()
    len_idx = [(word, len(word), idx) for idx, word in enumerate(list_of_strings)]
    max_e = max(len_idx, key=lambda x: (x[1], x[2]))
    return max_e[0]


# examples:
print(longest_word('a b c d e fgh'))  # fgh
print(longest_word('one two three'))  # three
print(longest_word('red blue grey'))  # grey
