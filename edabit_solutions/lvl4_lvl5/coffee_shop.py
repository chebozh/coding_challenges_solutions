"""Coffee Shop

Write a class called CoffeeShop, which has three instance variables:

    name : a string (basically, of the shop)
    menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a
    food or a drink) and price.
    orders : an empty list

and seven methods:

    add_order: adds the name of the item to the end of the orders list if it exists on the menu, otherwise, return
    "This item is currently unavailable!"
    fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty,
     return "All orders have been fulfilled!"
    list_orders: returns the item names of the orders taken, otherwise, an empty list.
    due_amount: returns the total amount due for the orders taken.
    cheapest_item: returns the name of the cheapest item on the menu.
    drinks_only: returns only the item names of type drink from the menu.
    food_only: returns only the item names of type food from the menu.

IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order.
Examples

tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
# Tesha's coffee shop does not sell hot cocoa
tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
# specifying the variant of "iced tea" will help the process

tcs.add_order("cinnamon roll") ➞  "Order added!"
tcs.add_order("iced coffee") ➞ "Order added!"
tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
# all items of the current order

tcs.due_amount() ➞ 2.17

tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
tcs.fulfill_order() ➞ "The iced coffee is ready!"
tcs.fulfill_order() ➞ "All orders have been fulfilled!"
# all orders have been presumably served

tcs.list_orders() ➞ []
# an empty list is returned if all orders have been exhausted

tcs.due_amount() ➞ 0.0
# no new orders taken, expect a zero payable

tcs.cheapest_item() ➞ "lemonade"
tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea",
 "vanilla chai latte", "hot chocolate", "iced coffee"]
tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]

Notes

Round off due amount up to two decimal places.

"""


class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name: str = name
        self.menu: list[dict] = menu
        self.orders: list[str] = orders

    def add_order(self, order: str) -> str:
        if order in {item['name'] for item in self.menu}:
            self.orders.append(order)
            return "Order added!"
        return "This item is currently unavailable!"

    def fulfill_order(self) -> str:
        if self.orders:
            return f"The {self.orders.pop(0)} is ready!"
        return "All orders have been fulfilled!"

    def list_orders(self) -> list:
        return [order for order in self.orders]

    def due_amount(self) -> float:
        if self.orders:
            ordered_items = [item for item in self.menu if item['name'] in self.orders]
            return round(sum(oitem['price'] for oitem in ordered_items), 2)
        else:
            return 0.0

    def cheapest_item(self) -> str:
        item = min(self.menu, key=lambda x: x['price'])
        return item['name']

    def drinks_only(self) -> list[str]:
        return [item['name'] for item in self.menu if item['type'] == 'drink']

    def food_only(self) -> list[str]:
        return [item['name'] for item in self.menu if item['type'] == 'food']


if __name__ == '__main__':
    m2 = [
        ["turkey english muffin", "food", 7.99], ["avocado toast", "food", 5.05],
        ["chocolate croissant", "food", 3.00],
        ["espresso", "drink", 2.99], ["iced caramel macchiato", "drink", 4.50], ["cortado", "drink", 4.00],
        ["nitro cold brew tester", "drink", 8.00]
    ]
    menu2 = [{'name': x[0], 'type': x[1], 'price': x[2]} for x in m2]

    shopy = CoffeeShop('Deep Into Coffee', menu2, list())
    assert shopy.add_order("cortado") == "Order added!"
    assert shopy.fulfill_order() == "The cortado is ready!"
    assert shopy.fulfill_order() == "All orders have been fulfilled!"
    assert shopy.add_order("avocado toast") == "Order added!"
    assert shopy.list_orders() == ["avocado toast"]
    assert shopy.due_amount() == 5.05
    assert shopy.cheapest_item() == "espresso"
    assert shopy.drinks_only() == ["espresso", "iced caramel macchiato", "cortado", "nitro cold brew tester"]
    assert shopy.food_only() == ["turkey english muffin", "avocado toast", "chocolate croissant"]

    m3 = [
        ["cheeseburger with fries", "food", 5.44],
        ["cinnamon roll", "food", 4.99],
        ["hot chocolate", "drink", 2.99],
        ["lemon tea", "drink", 2.50],
        ["iced coffee", "drink", 3.00],
        ["vanilla chai latte", "drink", 4.00]
    ]
    menu3 = [{'name': x[0], 'type': x[1], 'price': x[2]} for x in m3]

    shopz = CoffeeShop("Tesha's", menu3, list())
    assert shopz.add_order("hot cocoa") == "This item is currently unavailable!"
    assert shopz.due_amount() == 0.0
    assert shopz.add_order("cheeseburger with fries") == "Order added!"
    assert shopz.add_order("lemon tea") == "Order added!"
    assert shopz.add_order("iced coffee") == "Order added!"
    assert shopz.list_orders() == ["cheeseburger with fries", "lemon tea", "iced coffee"]
    assert shopz.due_amount() == 10.94
    assert shopz.fulfill_order() == "The cheeseburger with fries is ready!"
    assert shopz.fulfill_order() == "The lemon tea is ready!"
    assert shopz.fulfill_order() == "The iced coffee is ready!"
    assert shopz.list_orders() == []
    assert shopz.cheapest_item(), "lemon tea"
    assert shopz.drinks_only() == ["hot chocolate", "lemon tea", "iced coffee", "vanilla chai latte"]
    assert shopz.food_only() == ["cheeseburger with fries", "cinnamon roll"]
