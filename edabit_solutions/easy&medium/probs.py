"""Probabilities (Part 1)

Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than
 or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples

probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0

Notes

Probability of event = (num of favourable outcomes) / (total num of possible outcomes)
"""


# solution
def probability(lst, n):
    len_lst = len(lst)
    return round(len([e for e in lst if e >= n]) / len_lst * 100, 1)


if __name__ == '__main__':
    assert probability([5, 1, 8, 9], 6) == 50.0
    assert probability([7, 4, 17, 14, 12, 3], 16) == 16.7
    assert probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) == 70.0
