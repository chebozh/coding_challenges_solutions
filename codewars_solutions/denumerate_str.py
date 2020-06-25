"""You have to rebuild a string from an enumerated list. For this task, you have to check if input is correct beforehand.

    Input must be a list of tuples
    Each tuple has two elements.
    Second element is an alphanumeric character.
    First element is the index of this character into the reconstructed string.
    Indexes start at 0 and have to match with output indexing: no gap is allowed.
    Finally tuples aren't necessarily ordered by index.

If any condition is invalid, the function should return False.

Input example:

[(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]

Returns

'monty'

Available at: https://www.codewars.com/kata/denumerate-string/train/python
"""


# solution
def denumerate(enum_list):
    if enum_list and isinstance(enum_list, list):
        if all(isinstance(item, tuple) for item in enum_list):
            if all(len(item) == 2 for item in enum_list):
                if all(isinstance(item[0], int) and (len(item[1]) == 1 and item[1].isalnum()) for item in enum_list):
                    new_str = ''.join([i[1] for i in sorted(enum_list)])
                    if all(item[0] == new_str.find(item[1]) or item[0] == new_str.rfind(item[1]) for item in sorted(enum_list)):
                        return new_str
    return False


# Examples
print(denumerate([(4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')]))
print(denumerate([(0, 'a'), (1, 'bc')]))
print(denumerate([(1, '3'), (2, 'l'), (4, 'o'), (3, 'l'), (0, 'h')]))
