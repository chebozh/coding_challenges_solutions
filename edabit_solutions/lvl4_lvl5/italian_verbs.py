"""Learn Italian Verbs!

Most Italian verbs fall into one of three categories: those ending in are, those ending in ere, and those ending in ire.
How a verb is inflected depends on what category it belongs to.

A simple way to inflect an Italian verb is: delete the are/ere/ire ending to get the verb base, append a part specific
to its category, and append a part common to all verbs. For example, this is the Present Simple of three verbs for the
plural you (Italian voi):

    Amare (To love): Voi amate (you love) ➞ Specific: a, common: te
    Credere (To believe): Voi credete (you believe) ➞ Specific: e, common: te
    Dormire (To sleep): Voi dormite (you sleep) ➞ Specific: i, common: te

Create a function that takes in three parameters and returns an inflected verb with the appropriate pronoun.
The input will be an Italian verb, a person (first, second, third) and a number (singular, plural).

You'll be given three dictionaries: one with the Italian pronouns, one with the common part, and one with the specific
part. For the first two, the number will be nested within the person. For the third, you will also find lists as
values for the specific part of verbs ending in are, ere, and ire respectively.

Examples

inflect("amare", "first", "pl") ➞ "Noi amiamo"
# Pronoun: "Noi" + verb base: "am" + specific part: "ia" + common part: "mo"

inflect("credere", "third", "sing") ➞ "Lui/Lei crede"
# Pronoun: "Lui/Lei" + verb base: "cred" + specific part: "e" + common part: None

inflect("dormire", "sec", "pl") ➞ "Voi dormite"
# Pronoun: "Voi" + verb base: "dorm" + specific part: "i" + common part: "te"

Notes

    The dictionary for the pronouns is called pronomi.
    The dictionary for the specific part is called verbi_spec.
    The dictionary for the common part is called verbi_com.
"""

import re


def inflect(verb, person, number):
    pronomi = {
        'first': {'sing': 'Io', 'pl': 'Noi'},
        'sec': {'sing': 'Tu', 'pl': 'Voi'},
        'third': {'sing': 'Lui/Lei', 'pl': 'Loro'}}

    verbi_spec = {
        'first': {'sing': ['o', 'o', 'o'], 'pl': ['ia', 'ia', 'ia']},
        'sec': {'sing': ['i', 'i', 'i'], 'pl': ['a', 'e', 'i']},
        'third': {'sing': ['a', 'e', 'e'], 'pl': ['a', 'o', 'o']}}

    verbi_com = {
        'first': {'sing': '', 'pl': 'mo'},
        'sec': {'sing': '', 'pl': 'te'},
        'third': {'sing': '', 'pl': 'no'}}

    pattern = re.compile(r'[a|e|i]re')
    group = ('a', 'e', 'i').index(pattern.search(verb).group()[0])
    pronoun = pronomi[person][number]
    base = pattern.sub('', verb)
    specific_part = verbi_spec[person][number][group]
    common_part = verbi_com[person][number]
    return f'{pronoun} {base}{specific_part}{common_part}'


if __name__ == '__main__':
    assert inflect("dormire", "sec", "pl") == "Voi dormite"
    # Pronoun: "Voi" + verb base: "dorm" + specific part: "i" + common part: "te"
    assert inflect("credere", "third", "sing") == "Lui/Lei crede"
    # Pronoun: "Lui/Lei" + verb base: "cred" + specific part: "e" + common part: None
    assert inflect("amare", "first", "pl") == "Noi amiamo"
    # Pronoun: "Noi" + verb base: "am" + specific part: "ia" + common part: "mo"
