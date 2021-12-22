"""Keyword Cipher

A Keyword Cipher is a monoalphabetic cipher which uses a keyword to provide encryption on given string of message.

Create a function that takes two arguments: a string message and a string key, and returns an encoded message.

For the encryption key, the keyword is placed at the beginning, followed by the rest of the characters in the alphabet in order (in other words, with the keyword characters removed):

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

The encrypted message substitutes each plaintext character with the encryption key character in the corresponding position.

Return the given message encrypted against the key:

eMessage = "KEYABC"
// A = K, B = E, C = Y, H = A, I = B, J = C

Examples

keyword_cipher("keyword", "abchij") ➞ "keyabc"

keyword_cipher("purplepineapple", "abc") ➞ "pur"

keyword_cipher("mubashir", "edabit") ➞ "samucq"

Notes

    Don't forget to remove duplicates after concatenating string with keyword.
    Non-alphabetic characters must be left as they are.
"""
from string import ascii_lowercase


def keyword_cipher(key, message):
    keyword_alphabet = list(ascii_lowercase)

    key_chars = []
    for ch in key:
        if ch not in key_chars:
            key_chars.append(ch)

    for ch in key_chars:
        if ch in keyword_alphabet:
            keyword_alphabet.pop(keyword_alphabet.index(ch))

    keyword_alphabet = key_chars + keyword_alphabet
    res = []
    for ch in message:
        if ch in keyword_alphabet:
            idx = ascii_lowercase.index(ch)
            res.append(keyword_alphabet[idx])
        else:
            res.append(ch)

    return ''.join(res)


if __name__ == '__main__':
    assert keyword_cipher("tfozcivbsjhengarudlkpwqxmy", "a_bc&*83") == "t_fo&*83"

    assert keyword_cipher("purplepineapple", "xyz") == "xyz"

    assert keyword_cipher("keyword", "abchij") == "keyabc"

    assert keyword_cipher("purplepineapple", "abc") == "pur"

    assert keyword_cipher("mubashir", "edabit") == "samucq"
