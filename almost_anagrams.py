"""
Given two words, how many letters do you have to remove from them to make them anagrams?
Example

    First word : c od e w ar s (4 letters removed)
    Second word : ha c k er r a nk (6 letters removed)
    Result : 10

Hints

    A word is an anagram of another word if they have the same letters (usually in a different order).
    Do not worry about case. All inputs will be lowercase.


"""


# solution

def anagram_difference(w1, w2):
    return helper(w1, w2) + helper(w2, w1)


def helper(a, b):
    num = 0
    visited = []
    for l in a:
        if l not in b:
            num += 1
        else:
            if l not in visited:
                if a.count(l) > b.count(l):
                    num += a.count(l) - b.count(l)
                    visited.append(l)
    return num


# example
print(anagram_difference('codewars', 'hackerrank'))
print(anagram_difference('ab', 'ba'))
print(anagram_difference('pwslhderflpybdjhdwxtyeigbeppnun', 'nwpqwickfpgnazzuqkmrlyrrdizvoxxgniazqvv'))


