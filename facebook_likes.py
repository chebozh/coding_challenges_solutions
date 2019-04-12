"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
 like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.
"""


# solution
def likes(names):
    length = len(names)

    if length == 0:
        return "no one likes this"
    elif length == 1:
        return '{} likes this'.format(names[0])
    elif length == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif length == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:  # length > 3
        rest = len(names[2:])
        return '{}, {} and {} others like this'.format(names[0], names[1], rest)


# examples
print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
