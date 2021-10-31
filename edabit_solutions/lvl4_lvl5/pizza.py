"""Freshly Made Pizzas

Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
 Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the
ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.

Name	Ingredients
hawaiian	ham, pineapple
meat_festival	beef, meatball, bacon
garden_feast	spinach, olives, mushroom
Examples

p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2

p1.ingredients ➞ ["bacon", "parmesan", "ham"]

p2.ingredients ➞ ["spinach", "olives", "mushroom"]

p1.order_number ➞ 1

p2.order_number ➞ 2

Notes

    All words are given in lowercase.
"""


class Pizza:
    order_number = 1

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self.order_number = Pizza.order_number
        Pizza.order_number += 1

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


if __name__ == '__main__':
    p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
    p2 = Pizza.garden_feast()  # order 2

    assert p1.ingredients == ["bacon", "parmesan", "ham"]

    assert p2.ingredients == ["spinach", "olives", "mushroom"]

    assert p1.order_number == 1

    assert p2.order_number == 2
