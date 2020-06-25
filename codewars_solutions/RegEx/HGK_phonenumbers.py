"""
In Hong Kong, a valid phone number has the format xxxx xxxx where x is a decimal digit (0-9). For example:

"1234 5678" // is valid
"2359 1478" // is valid
"85748475" // invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756" // invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" // clearly invalid
"     1234 5678   " // is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl2839472398
jsfss2343242kldjf23423423SDLKFJSLKsdklf" // also contains a valid HK phone number (9345 8234)

Task

Define two functions, isValidHKPhoneNumber and hasValidHKPhoneNumber, that returns whether a given string is a valid HK
phone number and contains a valid HK phone number respectively (i.e. true/false values).
"""
# solution
import re


def is_valid_HK_phone_number(number):
    return bool(re.match(r'\d{4}\s\d{4}$', number))


def has_valid_HK_phone_number(number):
    return bool(re.search(r'\d{4}\s\d{4}', number))


# examples

print(is_valid_HK_phone_number("1234 5678"))  # True)
print(is_valid_HK_phone_number("2359 1478"))  # True)
print(is_valid_HK_phone_number("85748475"))  # False)
print(is_valid_HK_phone_number("3857  4756"))  # False)

print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678"))  # True)
print(has_valid_HK_phone_number("I wonder if 2359 1478 is a valid phone number?"))  # True)
print(has_valid_HK_phone_number("85748475 is definitely invalid"))  # , False)
print(has_valid_HK_phone_number("'3857  4756' is so close to a valid phone number!"))  # False)
