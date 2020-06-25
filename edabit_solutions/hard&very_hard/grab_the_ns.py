"""Grab the Numbers

Given a string including a bunch of characters and numbers, return the sum of all the numbers in the string.
Note that multiple digits next to each other are counted as a whole number rather than separate digits.

Examples

grab_number_sum('aeiou250abc10') ➞ 260

grab_number_sum('one1two2twenty20') ➞ 23

grab_number_sum('900uwu50uwuuwuuwu25uwu25') ➞ 1000

Notes
Remember not to just add single digit numbers together, it should be possible for answers to easily get into the 100s!
"""

# solution
import re


def grab_number_sum(s):
    nums = re.findall(r'\d+', s)
    return sum(int(n) for n in nums)


if __name__ == '__main__':
    assert grab_number_sum('aeiou250abc10') == 260

    assert grab_number_sum('one1two2twenty20') == 23

    assert grab_number_sum('900uwu50uwuuwuuwu25uwu25') == 1000
