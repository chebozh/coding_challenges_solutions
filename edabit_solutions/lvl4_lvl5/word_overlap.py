"""Word Overlapping

Given two words, overlap them in such a way, morphing the last few letters of the first word with the first few letters of the second word. Return the shortest overlapped word possible.
Examples

overlap("sweden", "denmark") ➞ "swedenmark"

overlap("edabit", "iterate") ➞ "edabiterate"

overlap("honey", "milk") ➞ "honeymilk"

overlap("dodge", "dodge") ➞ "dodge"

Notes

    All words will be given in lowercase.
    If no overlap is possible, return both words one after the other (example #3)."""


def overlap(s1: str, s2: str):
    if s1 == s2:
        return s1

    for i in range(len(s1)):
        if s2.startswith(s1[i:]):
            return s1[:i] + s2

    return s1 + s2


if __name__ == '__main__':
    assert overlap("sweden", "denmark") == "swedenmark"

    assert overlap("edabit", "iterate") == "edabiterate"

    assert overlap("honey", "milk") == "honeymilk"
    
    assert overlap("dodge", "dodge") == "dodge"
