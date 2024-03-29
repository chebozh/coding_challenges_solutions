"""Stock Picker

Create a function that takes a list of integers that represent the amount in dollars that a single stock is worth,
and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y>x.

If given the following list:

[44, 30, 24, 32, 35, 30, 40, 38, 15]

... your program should return 16 because at index 2 the stock was worth $24 and at the index 6 the stock was then
 worth $40, so if you bought the stock at 24 and sold it on 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.

If there is no profit that could have been made with the stock prices, then your program should return -1
(e.g. [[10, 9, 8, 2]] should return -1).

Examples

stock_picker([10, 12, 4, 5, 9]) ➞ 5

stock_picker([14, 20, 4, 12, 5, 11]) ➞ 8

stock_picker([80, 60, 10, 8]) ➞ -1"""

from itertools import combinations


def stock_picker(lst):
    profit_combos = [combo for combo in combinations(lst, 2) if combo[0] < combo[1]]
    if not profit_combos:
        return -1

    max_combo = max(profit_combos, key=lambda combo: combo[1] - combo[0])
    return max_combo[1] - max_combo[0]


if __name__ == '__main__':
    assert stock_picker([80, 60, 10, 8]) == -1

    assert stock_picker([10, 12, 4, 5, 9]) == 5

    assert stock_picker([14, 20, 4, 12, 5, 11]) == 8
