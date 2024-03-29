"""Splitting Objects Inside a List

You bought a few bunches of fruit over the weekend. Create a function that splits a bunch into singular objects inside a list.
Examples

split_bunches([
  { "name": "grapes", "quantity": 2 }
]) ➞ [
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 }
]


split_bunches([
  { "name": "currants", "quantity": 1 },
  { "name": "grapes", "quantity": 2 },
  { "name": "bananas", "quantity": 2 }
]) ➞ [
  { "name": "currants", "quantity": 1},
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 },
  { "name": "bananas", "quantity": 1 },
  { "name": "bananas", "quantity": 1 }
]

Notes

    The input list will never be empty.
    Objects will always have a name and quantity over 0.
    The returned object should have each fruit in the same order as the original.
"""


def split_bunches(bunches):
    res = []
    for bunch in bunches:
        for _ in range(bunch['quantity']):
            res.append({'name': bunch['name'], 'quantity': 1})
    return res


if __name__ == '__main__':
    assert split_bunches([
        {"name": "grapes", "quantity": 2}
    ]) == [
               {"name": "grapes", "quantity": 1},
               {"name": "grapes", "quantity": 1}
           ]

    assert split_bunches([
        {"name": "currants", "quantity": 1},
        {"name": "grapes", "quantity": 2},
        {"name": "bananas", "quantity": 2}
    ]) == [
               {"name": "currants", "quantity": 1},
               {"name": "grapes", "quantity": 1},
               {"name": "grapes", "quantity": 1},
               {"name": "bananas", "quantity": 1},
               {"name": "bananas", "quantity": 1}
           ]
