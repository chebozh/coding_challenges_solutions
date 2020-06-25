"""Identity Matrix

An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right.
 The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge,
if the integer is negative, return the mirror image of the identity matrix of n x n dimensions..
It does not matter if the mirror image is left-right or top-bottom.

Examples

id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []

Notes

Incompatible types passed as n should return the string "Error".
"""


def id_mtrx(n):
    if not isinstance(n, int):
        return 'Error'
    elif n == 0:
        return []

    matrix = []
    range_ = range(abs(n))
    for i in range_:
        r = [0 for _ in range_]
        if n > 0:
            r[i] = 1
        else:
            r[-1*(i+1)] = 1
        matrix.append(r)
    return matrix


if __name__ == '__main__':
    assert id_mtrx(2) == [
        [1, 0],
        [0, 1]
    ]

    assert id_mtrx(-2) == [
        [0, 1],
        [1, 0]
    ]

    assert id_mtrx(0) == []
