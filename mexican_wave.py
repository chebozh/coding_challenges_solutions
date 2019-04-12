"""In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
You will be passed a string and you must return that string in an array where an uppercase letter is a person
standing up.
Rules
  	1.  The input string will always be lower case but maybe empty.

2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
Example

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""


def wave(string):
    result = []
    for idx, char in enumerate(string):
        if char == " ":
            continue
        to_capitalize = string[idx: idx + 1]
        before = string[:idx]
        after = string[idx + 1:]
        mexican = '{}{}{}'.format(before, to_capitalize.upper(), after)
        result.append(mexican)
    return result


# example
print(wave("hello"))  # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave('two words'))
