"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

Examples:
Test.assert_equals(find_longest([1, 10, 100]), 100)
Test.assert_equals(find_longest([9000, 8, 800]), 9000)
Test.assert_equals(find_longest([8, 900, 500]), 900)

Available at: https://www.codewars.com/kata/most-digits/train/python
"""


# solution

def find_longest(arr):
    arr = [str(n) for n in arr]
    return int(max(arr, key=len))


# examples
print(find_longest([1, 10, 100]))
print(find_longest([9000, 8, 800]))
print(find_longest([8, 900, 500]))
