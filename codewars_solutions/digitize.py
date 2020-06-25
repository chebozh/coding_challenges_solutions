"""
Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]

Available at: https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""


# solution
def digitize(n):
    return [int(x) for x in reversed(str(n))]


# Examples
print(digitize(35231))
print(digitize(348597))
