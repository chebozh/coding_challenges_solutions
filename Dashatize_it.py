"""
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string
with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

"""


# solution
def dashatize(num):
    if num is None:
        return 'None'
    elif num < 0:
        num *= -1

    nums_s_l = [x for x in str(num)]
    if len(nums_s_l) == 1:
        return nums_s_l[0]

    result = ''
    for x in nums_s_l:
        if int(x) % 2 != 0:
            result += '-' + x + '-' if not result.endswith('-') else x + '-'
        else:
            result += x

    if result.startswith('-') and result.endswith('-'):
        return result[1:len(result) - 1]
    elif result.startswith('-'):
        return result[1:]
    elif result.endswith('-'):
        return result[:len(result) - 1]
    else:
        return result


# Examples
print(dashatize(274))
print(dashatize(6815))
