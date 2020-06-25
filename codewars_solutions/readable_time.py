"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format
(HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

https://www.codewars.com/kata/52685f7382004e774f0001f7
"""


# solution
def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


# Examples
print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
