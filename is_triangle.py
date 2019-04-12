"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built
with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Available at: https://www.codewars.com/kata/is-this-a-triangle/train/python
"""


# solution
def is_triangle(a: int, b: int, c: int):
    largest = max(a, b, c)
    if c == largest:
        return (a + b) > c
    elif b == largest:
        return (a + c) > b
    elif a == largest:
        return (c + b) > a


# Examples
print(is_triangle(5, 1, 5))  # True, "didn't work when sides were 5, 1, 5
print(is_triangle(2, 2, 2))  # True, "didn't work when sides were 2, 2, 2
print(is_triangle(-1, 2, 3))  # False, "didn't work when sides were -1, 2, 3
print(is_triangle(1, -2, 3))  # False, "didn't work when sides were 1, -2, 3
