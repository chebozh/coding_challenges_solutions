"""Harshad Number

A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines
whether a number is a Harshad or not.

Examples

is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171

is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True"""

def is_harshad(n):
    digits_sum = sum(int(d) for d in str(n))
    return n % digits_sum == 0

if __name__ == '__main__':
    assert is_harshad(481) is True

    assert is_harshad(89) is False

    assert is_harshad(516) is True

    assert is_harshad(200) is True
