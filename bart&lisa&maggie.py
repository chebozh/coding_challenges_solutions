"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

Available here: https://www.codewars.com/kata/53368a47e38700bd8300030d
"""


# solution
def namelist(names):
    names_list = [name['name'] for name in names]
    length = len(names_list)
    if length == 0:
        return ''
    elif length == 1:
        return str(names_list[0])
    elif length == 2:
        return ' & '.join([names_list[0], names_list[1]])
    else:
        return ', '.join(names_list[: -1]) + ' & ' + names_list[-1]


# Examples

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# returns 'Bart, Lisa & Maggie'

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# returns 'Bart & Lisa'

print(namelist([{'name': 'Bart'}]))
# returns 'Bart'

print(namelist([]))
# returns ''
