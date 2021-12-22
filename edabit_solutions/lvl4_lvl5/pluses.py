"""
Know Your Neighbor

Create a function that takes a string as an argument and returns True if each letter in the string is surrounded by a
plus sign. Return False otherwise.
Examples

plus_sign("+f+d+c+#+f+") ➞ True

plus_sign("+d+=3=+s+") ➞ True

plus_sign("f++d+g+8+") ➞ False

plus_sign("+s+7+fg+r+8+") ➞ False

Notes

For clarity, each letter must have a plus sign on both sides.
"""
def plus_sign(txt):
    if len(txt) <= 2:
        return False
    letters = [l for l in txt if l.isalpha()]
    for letter in letters:
        letter_idx = txt.index(letter)
        letter_prev = txt[letter_idx - 1]
        letter_next = txt[letter_idx + 1]
        if letter_prev != '+' or letter_next != '+':
            return False
    return True


if __name__ == '__main__':
    assert plus_sign("+f+d+c+#+f+") == True
    assert plus_sign("+d+=3=+s+") == True
    assert plus_sign("+d+k+##f+") == False
    assert plus_sign("hf+d++#+f+") == False
    assert plus_sign("+d+i+#+c+") == True
    assert plus_sign("a+") == False