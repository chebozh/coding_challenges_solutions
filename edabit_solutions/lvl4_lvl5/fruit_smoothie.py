"""Fruit Smoothie

Create a class Smoothie and do the following:

    Create an instance attribute called ingredients.
    Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
    Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5.
    Round to two decimal places.
    Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive
    sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie".
    Remember to change "-berries" to "-berry". See the examples below.

Ingredient	Price
Strawberries	$1.50
Banana	$0.50
Mango	$2.50
Blueberries	$1.00
Raspberries	$1.00
Apple	$1.75
Pineapple	$3.50
Examples

s1 = Smoothie(["Banana"])

s1.ingredients ➞ ["Banana"]

s1.get_cost() ➞ "$0.50"

s1.get_price() ➞ "$1.25"

s1.get_name() ➞ "Banana Smoothie"

s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])

s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]

s2.get_cost() ➞ "$3.50"

s2.get_price() ➞ "$8.75"

s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"
"""


class Smoothie:
    prices = {
        "Strawberries": "$1.50",
        "Banana": "$0.50",
        "Mango": "$2.50",
        "Blueberries": "$1.00",
        "Raspberries": "$1.00",
        "Apple": "$1.75",
        "Pineapple": "$3.50"
    }

    def __init__(self, ingredients):
        self._check_ingredient_availability(ingredients)
        self.ingredients = ingredients

    def get_cost(self):
        cost = sum(self._price_deformatted(self.prices[ingredient]) for ingredient in self.ingredients)
        return self._price_formatted(cost)

    def get_price(self):
        price = self._price_deformatted(self.get_cost())
        return self._price_formatted(round(price + (1.5 * price), 2))

    def get_name(self):
        ingredients = list(map(self._berries_to_berry, self.ingredients))
        if len(ingredients) == 1:
            res = f'{ingredients[0]} Smoothie'
        else:
            res = f'{" ".join(sorted(ingredients))} Fusion'
        return res

    def _check_ingredient_availability(self, ingredients):
        unavailable_ingredients = [ingr for ingr in ingredients if ingr not in self.prices]
        if unavailable_ingredients:
            raise ValueError(f'{", ".join(unavailable_ingredients)} not available.')

    @staticmethod
    def _price_deformatted(price):
        return float(price.replace('$', ''))

    @staticmethod
    def _price_formatted(price):
        return '${:.2f}'.format(price)

    @staticmethod
    def _berries_to_berry(ingredient):
        if 'berries' in ingredient:
            ingredient = ingredient.replace('berries', 'berry')
        return ingredient


if __name__ == '__main__':
    s1 = Smoothie(["Banana"])
    assert s1.ingredients == ["Banana"]
    assert s1.get_cost() == "$0.50"
    assert s1.get_price() == "$1.25"
    assert s1.get_name() == "Banana Smoothie"

    s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
    assert s2.ingredients == ["Raspberries", "Strawberries", "Blueberries"]
    assert s2.get_cost() == "$3.50"
    assert s2.get_price() == "$8.75"
    assert s2.get_name() == "Blueberry Raspberry Strawberry Fusion"

    import pytest
    with pytest.raises(ValueError):
        s3 = Smoothie(["Grapes"])
    with pytest.raises(ValueError):
        s4 = Smoothie(['Grapes', 'Papaya'])
