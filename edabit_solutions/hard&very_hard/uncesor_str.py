"""
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily,
I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.
Example

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes

The number of vowels will match the number of * characters in the censored string.
"""


# solution
def uncensor(txt, vowels):
    letters = list(txt)
    idx = -1
    for i in range(len(letters)):
        if letters[i] == '*':
            idx += 1
            letters[i] = vowels[idx]
    return ''.join(letters)


if __name__ == '__main__':
    assert uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") == "Where did my vowels go?"

    assert uncensor("abcd", "") == "abcd"

    assert uncensor("*PP*RC*S*", "UEAE") == "UPPERCASE"
