"""Create a function that takes an integer and returns it as an ordinal number.
An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th etc.
Examples

return_end_of_number(553) ➞ "553-RD"

return_end_of_number(34) ➞ "34-TH"

return_end_of_number(1231) ➞ "1231-ST"

return_end_of_number(22) ➞ "22-ND"
"""


def return_end_of_number(num):
    table = {
        ('1',): '-ST',
        ('2',): '-ND',
        ('3',): '-RD',
        ('0', '4', '5', '6', '7', '8', '9',): '-TH',
    }
    for k in table.keys():
        if str(num)[-1] in k:
            return str(num) + table[k]


if __name__ == '__main__':
    assert return_end_of_number(553) == "553-RD"

    assert return_end_of_number(34) == "34-TH"

    assert return_end_of_number(1231) == "1231-ST"

    assert return_end_of_number(22) == "22-ND"
