"""Add Two String Numbers

Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
Examples

add_str_nums("4", "5") ➞ "9"

add_str_nums("abcdefg", "3") ➞ "-1"

add_str_nums("1", "") ➞ "1"

add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ 1874682736267235927391936562808774986

Notes

If there are any non-numerical characters, return "-1".
If one option is blank the code should still work.
Python supports the addition of integers without limit, try this challenge without using this functionality.
Your function doesn't have to add negative numbers.
"""


def scale_tip(lst):
    mid = len(lst) // 2
    left_sum = sum(lst[:mid])
    right_sum = sum(lst[mid+1:])

    if left_sum > right_sum:
        return 'left'
    elif left_sum < right_sum:
        return 'right'
    return 'balanced'


if __name__ == '__main__':
    assert scale_tip([0, 0, "I", 1, 1]) == "right"
    assert scale_tip([1, 2, 3, "I", 4, 0, 0]) == "left"
    assert scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) == "balanced"
