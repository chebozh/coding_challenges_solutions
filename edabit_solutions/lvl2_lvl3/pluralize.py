"""
Pluralize!

Given a list of words in the singular form, return a set of those words in the plural form if they appear more than
once in the list.

Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes

    This is an oversimplification of the English language so no edge cases will appear.
    Only focus on whether or not to add an s to the ends of words.
    All tests will be valid.
"""
def pluralize(lst):
    return {w + "s" if lst.count(w)>1 else w for w in lst}

if __name__ == '__main__':
    assert pluralize(["cow", "pig", "cow", "cow"]) == {"cows", "pig"}

    assert pluralize(["table", "table", "table"]) == {"tables"}

    assert pluralize(["chair", "pencil", "arm"]) == {"chair", "pencil", "arm"}
