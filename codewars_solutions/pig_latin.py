"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
 untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""


# solution
def pig_it(text):
    text_list = [word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()]
    return ' '.join(text_list)


# examples
print(pig_it('Pig latin is cool'))
print(pig_it('O tempora o mores !'))
