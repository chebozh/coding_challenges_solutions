"""
Add Dollar Bills

Create a function that takes a string containing money in dollars and pounds sterling (seperated by comma)
and returns the sum of dollar bills only, as an integer.

For the input string:

    Each amount is prefixed by the currency symbol: $ for dollars and £ for pounds.
    Thousands are represented by the suffix k.

i.e. $4k = $4,000 and £40k = £40,000
Examples

add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70

add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170

add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200

Notes

There is at least one dollar bill in string.
"""

import re


def add_bill(money):
    dollars = re.findall(r'd([a-z0-9_.-]+)', money)
    f = lambda x: int(x.replace('k', '000')) if 'k' in x else int(x)
    dollars = [f(amount) for amount in dollars]
    return sum(dollars)


if __name__ == '__main__':
    assert add_bill("d20,p40,p60,d50") == 70

    assert add_bill("p30,d20,p60,d150,p360") == 170

    assert add_bill("p30,d2k,p60,d200,p360") == 2200
