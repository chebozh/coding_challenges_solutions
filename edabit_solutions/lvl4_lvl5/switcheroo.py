"""A Subtle Switcheroo

Create a function which replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.
Examples

switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"

switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."

switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

Notes

    Empty strings should return just an empty string (see example #2).
    Ignore punctuation and any instances where "nts" or "nce" are not at the end of a word (see example #3).
"""


def switcheroo(txt):
    return ' '.join(map(_replace, txt.split()))


def _replace(word):
    letters = ''.join(ch for ch in word if ch.isalpha())
    punctuation = word[len(letters):]
    if letters.endswith('nts'):
        letters = letters.replace('nts', 'nce')
    elif letters.endswith('nce'):
        letters = letters.replace('nce', 'nts')
    else:
        return word
    return letters + punctuation


if __name__ == '__main__':
    assert switcheroo("The elephants in France were chased by ants!") == "The elephance in Frants were chased by ance!"

    assert switcheroo("While he rants, I fall into a trance...") == "While he rance, I fall into a trants..."

    assert switcheroo("Bounced over the fence!") == "Bounced over the fents!"
