"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of
 characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
"""


# solution
def solution(s):
    n = 2
    return [s[i:i + n] if len(s[i:i + n]) == 2 else s[i:i + n] + '_' for i in range(0, len(s), n)]


# examples
print(solution('abc'))  # should return ['ab', 'c_']
print(solution('abcdef'))  # should return ['ab', 'cd', 'ef']
