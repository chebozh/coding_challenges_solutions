# Western Showdown
#
# Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his
# opponent in a gun standoff.
#
# Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return
# "tie".
#
# Examples
#
# showdown(
#   "   Bang!        ",
#   "        Bang!   "
# ) ➞ "p1"
#
# # p1 draws his gun sooner than p2
#
# showdown(
#   "               Bang! ",
#   "             Bang!   "
# ) ➞ "p2"
#
# showdown(
#   "     Bang!   ",
#   "     Bang!   "
# ) ➞ "tie"
#
# Notes
#
# Both strings are the same length.

def showdown(p1, p2):
    shot = 'Bang!'
    t1 = p1.index(shot)
    t2 = p2.index(shot)
    if t1 < t2:
        return 'p1'
    elif t1 > t2:
        return 'p2'
    else:
        return 'tie'


if __name__ == '__main__':
    assert showdown(
        "  Bang!   ",
        "Bang!     "
    ) == "p2"

    assert showdown(
        "   Bang!        ",
        "        Bang!   "
    ) == "p1"

    assert showdown(
    "               Bang! ",
    "             Bang!   "
    ) =="p2"

    assert showdown(
        "     Bang!   ",
        "     Bang!   "
    ) == "tie"