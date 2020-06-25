"""Filtering by Star Rating

Given a dictionary of some items with star ratings and a specified star rating, return a new dictionary of items
which match the specified star rating. Return "No results found" if no item matches the star rating given.

Examples

filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****") ➞ {
  "Luxury Chocolates" : "*****",
  "Aunty May Chocolates" : "*****"
}

filter_by_rating({
  "Continental Hotel" : "****",
  "Big Street Hotel" : "**",
  "Corner Hotel" : "**",
  "Trashviews Hotel" : "*",
  "Hazbins" : "*****"
}, "*") ➞ {
  "Trashviews Hotel" : "*"
}

filter_by_rating({
  "Solo Restaurant" : "***",
  "Finest Dinings" : "*****",
  "Burger Stand" : "***"
}, "****") ➞ "No results found"
"""


# solution
def filter_by_rating(d, rating):
    res = {item: irating for item, irating in d.items()
           if len(irating) == len(rating)}
    return res or "No results found"


if __name__ == '__main__':
    assert filter_by_rating({
        "Luxury Chocolates": "*****",
        "Tasty Chocolates": "****",
        "Aunty May Chocolates": "*****",
        "Generic Chocolates": "***"
    }, "*****") == {
        "Luxury Chocolates": "*****",
        "Aunty May Chocolates": "*****"
    }

    assert filter_by_rating({
        "Continental Hotel": "****",
        "Big Street Hotel": "**",
        "Corner Hotel": "**",
        "Trashviews Hotel": "*",
        "Hazbins": "*****"
    }, "*") == {
        "Trashviews Hotel": "*"
    }

    assert filter_by_rating({
        "Solo Restaurant": "***",
        "Finest Dinings": "*****",
        "Burger Stand": "***"
    }, "****") == "No results found"