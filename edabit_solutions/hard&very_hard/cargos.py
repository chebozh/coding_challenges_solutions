"""
Does the Cargo Fit? (Part 2)

A ship has to transport cargo from one place to another, while picking up cargo along the way.
Given the total amount of cargo and the types of cargo holds in the ship as lists, create a function that returns True
if each weight of cargo can fit in one hold, and False if it can't.

	"S" means 50 cargo space.
	"M" means 100 cargo space.
	"L" means 200 cargo space.

Examples

will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) ➞ True

will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) ➞ False

will_fit(["L", "L", "M"], [56, 62, 84, 90]) ➞ True


"""


def will_fit(holds, cargo):
    caps = {
        "S": 50,
        "M": 100,
        "L": 200,
    }
    cd = zip([caps[hold] for hold in holds], cargo)
    return not any(cap_hold[0] < cap_hold[1] for cap_hold in cd)


if __name__ == '__main__':
    assert will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) is True

    assert will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70, 80, 90, 200]) is False

    assert will_fit(["L", "L", "M"], [56, 62, 84, 90]) is True
