"""
Write a regular expression to match any article + noun pair. The articles are either "a/an" or "the".
Use non-capturing groups in your expression.
Example

txt = "There is an apple and a pen on the desk"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["an apple", "a pen", "the desk"]

Notes

    You don't need to write a function, just the pattern.
    Do not remove import re from the code.
    Find more info on RegEx and non-capturing groups in Resources.
"""
import re


def get_article_and_nouns(txt):
    return re.findall(r'\b(?:a|an|the)\s\w*', txt)


if __name__ == '__main__':
    txt1 = 'There is a pencil and a pen on the desk'
    txt2 = 'Breathe the air of the mountain'
    txt3 = 'He is Italian and she is French'

    assert get_article_and_nouns(txt1) == ['a pencil', 'a pen', 'the desk']
    assert get_article_and_nouns(txt2) == ['the air', 'the mountain']
    assert get_article_and_nouns(txt3) == []
