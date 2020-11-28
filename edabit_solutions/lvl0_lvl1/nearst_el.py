"""The Nearest Element

Given a list of integers lst, implement a function that returns the index of the number nearest to the given value n.
If two numbers equally distant from n are found, the function will return the greatest of them.

Examples

nearest_element(10, [1, 100, 1000]) ➞ 0
# 1 is the number nearest to 10.

nearest_element(50, [100, 49, 51]) ➞ 2
# 49 and 51 are equally distant from 50, with 51 being the greatest.

nearest_element(-20, [-50, -10, -30]) ➞ 1
# -10 and -30 are equally distant from -20, with -10 being the greatest.
"""


# solution
def nearest_element(n, lst):
    num_diff = {x: abs(x - n) for x in lst}
    smallest_diff = min(num_diff.values())
    smallest_diff_nums = [k for k, v in num_diff.items() if v == smallest_diff]
    return lst.index(max(smallest_diff_nums))


if __name__ == '__main__':
    assert nearest_element(10, [1, 100, 1000]) == 0
    # 1 is the number nearest to 10.

    assert nearest_element(50, [100, 49, 51]) == 2
    # 49 and 51 are equally distant from 50, with 51 being the greatest.

    assert nearest_element(-20, [-50, -10, -30]) == 1
    # -10 and -30 are equally distant from -20, with -10 being the greatest.
