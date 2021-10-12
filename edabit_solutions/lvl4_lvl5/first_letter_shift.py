"""First Letter Shift

Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).
Examples

shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"

Notes

    The last word shifts its first letter to the first word in the sentence.
    All sentences will be given in lowercase.
    Note how single words remain untouched (example #4).
"""


def shift_sentence(txt):
    words = txt.split()
    if len(words) == 1:
        return txt
    res = []
    for i, _ in enumerate(words):
        word_chars = [ch for ch in words[i]]
        prev_word_chars = [ch for ch in words[i - 1]]
        word_chars[0] = prev_word_chars[0]
        res.append(''.join(word_chars))
    return ' '.join(res)


if __name__ == '__main__':
    assert shift_sentence("create a function") == "freate c aunction"

    assert shift_sentence("it should shift the sentence") == "st ihould shift she tentence"

    assert shift_sentence("the output is not very legible") == "lhe tutput os iot nery vegible"

    assert shift_sentence("edabit") == "edabit"
