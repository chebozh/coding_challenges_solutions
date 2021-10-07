"""Poker Hand Ranking

In this challenge, you have to establish which kind of Poker combination is present in a deck of five cards.
Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

"Ah" ➞ Ace of hearts
"Ks" ➞ King of spades
"3d" ➞ Three of diamonds
"Qc" ➞ Queen of clubs

There are 10 different combinations. Here's the list, in decreasing order of importance:
Name	Description
Royal Flush	A, K, Q, J, 10, all with the same suit.
Straight Flush	Five cards in sequence, all with the same suit.
Four of a Kind	Four cards of the same rank.
Full House	Three of a Kind with a Pair.
Flush	Any five cards of the same suit, not in sequence.
Straight	Five cards in a sequence, but not of the same suit.
Three of a Kind	Three cards of the same rank.
Two Pair	Two different Pair.
Pair	Two cards of the same rank.
High Card	No other valid combination.

Given a list hand containing five strings being the cards, implement a function that returns a string with the name of
the highest combination obtained, accordingly to the table above.
Examples

poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"

poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"

poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"
"""


def poker_hand_ranking(hand):
    hand = list(map(lambda x: x.replace('10', 'T'), hand))
    ranks = _card_ranks(hand)
    suits = {suit for _, suit in hand}

    if _is_royal_flush(ranks, suits):
        return 'Royal Flush'
    elif _is_straight_flush(ranks, suits):
        return 'Straight Flush'
    elif _is_n_of_kind(4, ranks):
        return 'Four of a Kind'
    elif _is_full_house(ranks):
        return 'Full House'
    elif _is_flush(suits):
        return 'Flush'
    elif _is_straight(ranks):
        return 'Straight'
    elif _is_n_of_kind(3, ranks):
        return 'Three of a Kind'
    elif _is_two_pair(ranks):
        return 'Two Pair'
    elif _is_n_of_kind(2, ranks):
        return 'Pair'
    else:
        return 'High Card'


def _card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, _ in hand]
    ranks.sort(reverse=True)
    return ranks


def _is_royal_flush(ranks, suits):
    if len(suits) == 1 and sorted(ranks) == list(range(10, 15)):
        return True
    return False


def _is_straight_flush(ranks, suits):
    if _is_straight(ranks) and _is_flush(suits):
        return True
    return False


def _is_n_of_kind(n, ranks):
    return any(ranks.count(rank) == n for rank in ranks)


def _is_full_house(ranks):
    return _is_n_of_kind(3, ranks) and _is_two_pair(ranks)


def _is_flush(suits):
    return len(suits) == 1


def _is_straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def _is_two_pair(ranks):
    pair_ranks = {rank for rank in ranks if ranks.count(rank) >= 2}
    return len(pair_ranks) == 2


if __name__ == '__main__':
    assert poker_hand_ranking(["Js", "Qs", "10s", "Ks", "As"]) == "Royal Flush"
    assert poker_hand_ranking(["10s", "9s", "8s", "6s", "7s"]) == "Straight Flush"
    assert poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) == "Four of a Kind"
    assert poker_hand_ranking(["10c", "9c", "9s", "10s", "9h"]) == "Full House"
    assert poker_hand_ranking(["Ad", "Kd", "Qd", "Jd", "9d"]) == "Flush"
    assert poker_hand_ranking(["10h", "Jh", "Qs", "Ks", "Ac"]) == "Straight"
    assert poker_hand_ranking(["Ac", "Qc", "As", "Ah", "2d"]) == "Three of a Kind"
    assert poker_hand_ranking(["8h", "8s", "As", "Qh", "Kh"]) == "Pair"
    assert poker_hand_ranking(["8h", "2h", "8s", "3s", "3c"]), "Two Pair"
    assert poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) == "High Card"
