"""John has invited people. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that

    makes this string uppercase
    gives it sorted in alphabetical order by last name. When the last names are the same, sort them by first name.
    Last name and first name of a guest come in the result between parentheses separated by a comma. So the result of
    function meeting(s) will be:
(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)

    It can happen that in two distinct families with the same family name two people have the same first name too.
"""
import re


def meeting(string):
    invitee_names = re.findall(r'(\w*):(\w*);?', string)
    invitee_names = [(n[1].upper(), n[0].upper()) for n in invitee_names]
    invitee_names = sorted(invitee_names, key=lambda fullname: (fullname[0], fullname[1]))

    result = ''
    for name in invitee_names:
        result += f'({name[0]}, {name[1]})'

    return result


# examples
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
print(meeting(s))
