"""
You are in the process of creating a chat application and want to add an anonymous name feature.
This anonymous name feature will create an alias that consists of two capitalized words beginning with the same letter
as the users first name.

Create a function that determines if the list of users is mapped to a list of anonymous names correctly.
"""


def is_correct_aliases(names, aliases):
    name_to_alias = dict(zip(names, aliases))
    for name, alias in name_to_alias.items():
        name = name.split()
        alias = alias.split()
        if name[0][0] != alias[0][0] or name[0][0] != alias[-1][0]:
            return False
    return True


if __name__ == '__main__':
    assert is_correct_aliases(['Adrian M.', 'Harriet S.', 'Mandy T.'],
                              ['Amazing Artichoke', 'Hopeful Hedgehog', 'Marvelous Mouse']) is True

    assert is_correct_aliases(['Rachel F.', 'Pam G.', 'Fred Z.', 'Nancy K.'],
                              ['Reassuring Rat', 'Peaceful Panda', 'Fantastic Frog', 'Notable Nickel']) is True
