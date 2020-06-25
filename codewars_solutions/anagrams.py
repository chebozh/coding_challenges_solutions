"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array
 with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""


# solution
def get_counts(word):
    word_count = {}
    for char in word:
        if char in word_count.keys():
            word_count[char] += 1
        else:
            word_count[char] = 1
    return word_count


def anagrams(word, words):
    word_counts = get_counts(word)
    result = []
    for w in words:
        if get_counts(w) == word_counts:
            result.append(w)
    return result


# Examples
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
