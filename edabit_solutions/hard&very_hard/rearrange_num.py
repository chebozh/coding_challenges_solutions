"""Rearrange the Number

Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are
rearranged.

Examples

rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
"""


def rearranged_difference(num):
    n = ''.join(sorted(str(num)))
    return int(n[::-1]) - int(n)


if __name__ == '__main__':
    assert rearranged_difference(972882) == 760833
    # 988722 - 227889 = 760833

    assert rearranged_difference(3320707) == 7709823
    # 7733200 - 23377 = 7709823

    assert rearranged_difference(90010) == 90981
    # 91000 - 19 = 90981
