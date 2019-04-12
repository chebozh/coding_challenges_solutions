"""
Your task is to remove all duplicate words from string, leaving only single words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

7kuy
"""
# solution
import re
import time


def remove_duplicate_words(s):
    res = ''

    for w in re.findall(r'\w+', s):
        if w not in res:
            res += w + ' '

    return res.rstrip()

# examples
print(remove_duplicate_words("my cat is my cat fat"))
print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


