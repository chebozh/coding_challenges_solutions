"""pigLatin2.0

https://edabit.com/challenge/v2r4rY7qv4ejc4SeQ

Rules for converting to pig latin:

For words that begin with a vowel (a, e, i, o, u), add "way" Otherwise, move all letters before the first vowel to the
end and add "ay" Use the function isVowel() coded in the previous question to help code this function.
You may assume there is at least one vowel in the input. You need to copy and past your code for isVowel() here.

pigLatin('attack') → 'attackway'
pigLatin('on') → 'onway'
pigLatin('friday') → 'idayfray'
"""


# solution
def pig_latin(user_input):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for v in vowels:
        if user_input.startswith(v):
            return '{}{}'.format(user_input, 'way')
    for i, ch in enumerate(user_input):
        if ch in vowels:
            return '{}{}{}'.format(user_input[i:], user_input[:i], 'ay')


if __name__ == '__main__':
    assert pig_latin('attack') == 'attackway'
    assert pig_latin('on') == 'onway'
    assert pig_latin('friday') == 'idayfray'
