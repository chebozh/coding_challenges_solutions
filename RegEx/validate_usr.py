"""
Write a simple regex to validate a username. Allowed characters are:

    lowercase letters,
    numbers,
    underscore

Length should be between 4 and 16 characters (both included).

8kuy
"""

import re


# solution
def validate_usr(username):
    usr_len = len(username)
    anti_pattern = re.search(r'[^a-z0-9_]', username)

    if usr_len < 4 or usr_len > 16 or anti_pattern:
        return False
    else:
        return True

# examples
print(validate_usr('asddsa'))
print(validate_usr('a'))
print(validate_usr('Hass'))
print(validate_usr('Hasd_12assssssasasasasasaasasasasas'))
print(validate_usr(''))
print(validate_usr('____'))
print(validate_usr('012'))
print(validate_usr('p1pp1'))
print(validate_usr('asd43 34'))
print(validate_usr('asd43_34'))
