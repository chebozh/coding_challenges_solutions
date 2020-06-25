"""
You are given a list of strings consisting of grocery items,
with prices in parentheses. Return a list of prices in float format.
"""

import re


def get_prices(lst):
    prices = []
    pattern = re.compile(r'\(\$(\d+\.\d+)')
    for s in lst:
        price = pattern.findall(s)
        if price:
            prices.append(float(price[0]))
    return prices


if __name__ == '__main__':
    assert get_prices(['pizza ($2.99)', 'shampoo ($15.75)', 'trash bags ($15.00)']) == [2.99, 15.75, 15.0]
