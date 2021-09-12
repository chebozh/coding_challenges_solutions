"""
Hashtag Generator

Create a function that is a Hashtag Generator by using the following rules:

    The output must start with a hashtag (#).
    Each word in the output must have its first letter capitalized.
    If the final result, a single string, is longer than 140 characters, the function should return false.
    If either the input (str) or the result is an empty string, the function should return false.

Examples

generate_hashtag("    Hello     World   ") ➞ "#HelloWorld"

generate_hashtag("") ➞ false, "Expected an empty string to return false"

generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."
"""


def generate_hashtag(txt: str):
    if not txt or txt.isspace():
        return False

    res = '#{}'.format(''.join(w.capitalize() for w in txt.split()))
    return res if len(res) <= 140 else False


if __name__ == '__main__':
    assert generate_hashtag("    Hello     World   ") == "#HelloWorld"

    assert generate_hashtag("") is False

    assert generate_hashtag("Edabit Is Great") == "#EdabitIsGreat", "Should remove spaces."
