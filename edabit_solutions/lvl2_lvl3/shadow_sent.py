"""
Shadow Sentences

Given two sentences, return whether they are shadows of each other. This means that all of the word lengths are the same,
 but the corresponding words don't share any common letters.

Examples

shadow_sentence("they are round", "fold two times") ➞ True

shadow_sentence("own a boat", "buy my wine") ➞ False
# No words share common letters, but "a" and "my" have different lengths.

shadow_sentence("his friends", "our company") ➞ False
# Word lengths are the same but "friends" and "company" share the letter "n".

shadow_sentence("salmonella supper", "birthright") ➞ False
# Setences with different numbers of words.

Notes

    All sentences will be given in lowercase, and will have no punctuation.
    Return False if the sentences have different numbers of words.
"""


def shadow_sentence(a, b):
    a_lst = a.split()
    b_lst = b.split()

    if len(a_lst) != len(b_lst):
        return False

    for w_a, w_b in zip(a_lst, b_lst):
        if len(w_a) != len(w_b) or any(l in w_b for l in w_a):
            return False
    return True


if __name__ == '__main__':
    assert shadow_sentence("they are round", "fold two times") is True

    assert shadow_sentence("own a boat", "buy my wine") is False
    # No words share common letters, but "a" and "my" have different lengths.

    assert shadow_sentence("his friends", "our company") is False
    # Word lengths are the same but "friends" and "company" share the letter "n".

    assert shadow_sentence("salmonella supper", "birthright") is False
    # Setences with different numbers of words.
