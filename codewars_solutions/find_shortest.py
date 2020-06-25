"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
Available at: https://www.codewars.com/users/chebozh/completed_solutions
"""


# solution
def find_short(s):
    s = s.split()
    l = len(s[0])
    for word in s:
        current_word_l = len(word)
        if current_word_l < l:
            l = current_word_l
    return l  # l: shortest word length


# examples
print(find_short("bitcoin take over the world maybe who knows perhaps"))  # shd be 3
print(find_short("turns out random test cases are easier than writing out basic ones"))  # shd be 3
print(find_short("i want to travel the world writing code one day"))  # shd be 1
print(find_short("Lets all go on holiday somewhere very cold"))  # shd be 2
