"""
Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza they are going to divide the
costs.

If the pizza is less than €5,- Michael is paying. Kate will contribute no more than €10. Michael will pay at least 2/3
 of the costs.

How much is Michael going to pay? Remember to calculate the amount in euros, with two decimals if necessary.

Available here: https://www.codewars.com/kata/pizza-payments/train/python
"""


# solution
def michael_pays(costs):
    michael_contribution = 2 / 3
    kate_contribution = 10
    if costs < 5:
        return round(costs, 2)
    elif costs - (michael_contribution * costs) > kate_contribution:
        return round(costs - 10, 2)
    return round(michael_contribution * costs, 2)


# Examples
print(michael_pays(30))  # 20 expected
print(michael_pays(80))  # 70 expected
print(michael_pays(28.789))  # 19.19 expected
