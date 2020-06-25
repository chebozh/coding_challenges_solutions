"""Chocolate Dilemma

Agatha and Bertha are sisters eating chocolate given to them by their parents. Bertha has always suspected her parents
of considering Agatha as the favorite child. To settle this dispute once and for all, she decides to analyze all pieces
of chocolate split between them, and determine that if they both have an equal amount of chocolate, then no favoritism
 exists.

Create a function that returns true if the total amount of chocolate is identical for each sister. All chocolate are
given in rectangular pieces that are represented by a pair of coordinates for length and width. Sum up the total area of
 chocolate for each sister, and return true if the total area of chocolate is the same.

To illustrate:

test_fairness([[4, 3], [2, 4], [1,2]], [[6,2], [4,2], [1,1], [1,1]]) => True

Since the total area of Agatha's chocolate is:

4x3 + 2x4 + 1x2 = 12 + 8 + 2 = 22

And the total area of Bertha's chocolate is:

6x2 + 4x2 + 1x1 + 1x1 = 12 + 8 + 1 + 1 = 22
"""


# solution
def test_fairness(agatha, bertha):
    quantity_a = sum(x * y for x, y in agatha)
    quantity_b = sum(x * y for x, y in bertha)
    return quantity_a == quantity_b


if __name__ == '__main__':
    assert test_fairness([[4, 3], [2, 4], [1, 2]], [[6, 2], [4, 2], [1, 1], [1, 1]]) is True
    assert test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]) is False
