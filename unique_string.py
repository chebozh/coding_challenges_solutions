"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only
 spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
"""


# TODO Currently a n^2 solution - refactor
def find_uniq(arr):
    arr_lower = [l.lower() for l in arr]
    visited = [arr_lower[0]]
    not_visited = arr_lower[1:]

    for i, e in enumerate(arr_lower):
        if make_check(e, not_visited) or make_check(e, visited):
            return arr[i]
        else:
            visited.append(e)


def make_check(string, arr):
    for e in arr:
        if all(l in e for l in string):
            return False
    return True


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))
print(find_uniq(['', '', '', 'a', '', '']))
