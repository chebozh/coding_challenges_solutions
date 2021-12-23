"""Gaderypoluki Cipher

Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:

"gaderypoluki" -> "ga de ry po lu ki"

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used.

Return the encrypted message.

Examples

encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"""


def encrypt(key, message):
    key_by_two = [key[i:i + 2] for i in range(0, len(key), 2)]
    res = []

    for ch in message:
        if any(ch in pair for pair in key_by_two):
            pair = [p for p in key_by_two if ch in p][0]
            ch_idx = pair.index(ch)
            adj_ch = pair[1] if ch_idx == 0 else pair[0]
            res.append(adj_ch)
        else:
            res.append(ch)

    return ''.join(res)


if __name__ == '__main__':
    assert encrypt("ab c", "abc ab") == "ba cba"

    assert encrypt("otorhinolaryngological", "My name is Paul") == "Mr olme hs Plua"

    assert encrypt("gaderypoluki", "This is an encrypted message") == "Thks ks gn dncyrotde mdssgad"""
