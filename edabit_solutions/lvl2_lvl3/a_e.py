"""Pronouncing A_E

Words with a_e in them (where the underscore represents any letters) are pronounced like ay_.

Given a sentence, create a function which replaces all instances of a_e with a ay_.

Examples

pronounce_the_a_e('i want to bake a cake') ➞ 'i want to bayk a cayk'

pronounce_the_a_e('cinnamon flakes') ➞ 'cinnamon flayks'

pronounce_the_a_e('bravely escape and inflate') ➞ 'brayvly escayp and inflayt'

pronounce_the_a_e('waste and taste') ➞ 'wayst and tayst'

Notes

    All words will be given in lowercase and without punctuation.
"""
import re


def pronounce_the_a_e(txt):
    return re.sub(r'a([a-z]+)e', r'ay\1', txt)


if __name__ == '__main__':
    assert pronounce_the_a_e('i want to bake a cake') == 'i want to bayk a cayk'

    assert pronounce_the_a_e('cinnamon flakes') == 'cinnamon flayks'

    assert pronounce_the_a_e('bravely escape and inflate') == 'brayvly escayp and inflayt'

    assert pronounce_the_a_e('waste and taste') == 'wayst and tayst'
