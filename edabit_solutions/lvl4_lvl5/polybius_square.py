"""
Polybius Square (Basic)

The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid.
The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot
(as there are 26 letters and only 25 slots).

	1	2	3	4	5
1	A	B	C	D	E
2	F	G	H	I/J	K
3	L	M	N	O	P
4	Q	R	S	T	U
5	V	W	X	Y	Z

To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.
Examples

polybius("Hi") ➞ "2324"

polybius("2324  4423154215") ➞ "hi there"

polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

Notes

As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
"""


def polybius(text):
    square = {
        '1': ('A', 'B', 'C', 'D', 'E'),
        '2': ('F', 'G', 'H', 'I/J', 'K'),
        '3': ('L', 'M', 'N', 'O', 'P'),
        '4': ('Q', 'R', 'S', 'T', 'U'),
        '5': ('V', 'W', 'X', 'Y', 'Z'),
    }
    if all(w.isdecimal() for w in text.split(' ')):
        return _decipher(text, square)  # convert numbers to letters
    else:
        return _encipher(text, square)  # convert letters to numbers


def _decipher(text, square):
    res = []
    for word in text.split(' '):
        paired_numbers = [word[i:i + 2] for i in range(0, len(word), 2)]  # paired into 2 number chars
        deciphered_word = []
        for number in paired_numbers:
            idx_a, idx_b = number[0], int(number[1])
            row = square[idx_a]
            letter = row[idx_b - 1]
            letter = 'I' if letter == 'I/J' else letter
            deciphered_word.append(letter.lower())
        res.append(''.join(deciphered_word))
    return ' '.join(res)


def _encipher(text, square):
    res = []
    for letter in text.upper():
        for k, v in square.items():
            found = False
            for i, l in enumerate(v, start=1):
                if letter == l or letter in l.split('/'):
                    res.append('{}{}'.format(k, i))
                    found = True
                    break  # break out of inner loop
                elif letter.isspace():
                    res.append(letter)
                    found = True
                    break
            if found:
                break  # break out of outer loop
    return ''.join(res)


if __name__ == '__main__':
    assert polybius('The lesson is: never try') == '442315 311543433433 2443 3315511542 444254'
    assert polybius(
        "Just because I don't care doesn't mean that I don't understand") == \
           '24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314'
    assert polybius("Hi") == "2324"

    assert polybius('543445 14343344 522433 21422415331443 52244423 4311311114') == \
           'you dont win friends with salad'
