"""
Phrase or Word Inverse

Create a function that inverts words or the phrase depending on the value of parameter type. A "P" means to invert the
entire phrase, while a "W" means to invert every word in the phrase. See the following examples for clarity.
Examples

inverter("This is Valhalla", "P") ➞ "Valhalla is this"

inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"

inverter("Division by powers of two", "P") ➞ "Two of powers by division"

Notes

    The first character of the returned string should be in uppercase and the rest are in lowercase.
    There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness,
    are discounted in the input phrases.
"""


def inverter(txt, type_):
    words = txt.split()
    words_reversed = []

    if type_ == 'P':
        words_reversed = list(reversed(words))
        words_reversed[-1] = words_reversed[-1].lower()
    elif type_ == 'W':
        words_reversed = [''.join(reversed(word)) for word in words]

    words_reversed[0] = words_reversed[0].capitalize()
    return ' '.join(w for w in words_reversed)


if __name__ == '__main__':
    assert inverter("This is Valhalla", "P") == "Valhalla is this"

    assert inverter("One fine day to start", "W") == "Eno enif yad ot trats"

    assert inverter("Division by powers of two", "P") == "Two of powers by division"
