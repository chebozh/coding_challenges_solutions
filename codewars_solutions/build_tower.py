"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

    Python: return a list;

Available here: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
"""


# solution

def tower_builder(n_floors):
    tower = []
    spaces = n_floors - 1
    stars = 1
    for floor in range(n_floors):
        tower.append(spaces * ' ' + '*' * stars + spaces * ' ')
        spaces -= 1
        stars += 2
    return tower


# Examples
print(tower_builder(1))  # ['*', ]
print(tower_builder(2))  # [' * ', '***']
print(tower_builder(3))  # , ['  *  ', ' *** ', '*****']
