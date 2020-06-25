"""ou are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any
string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

#Example:

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) --> 13

Bash note:

input : 2 strings with substrings separated by ,

output: number as a string

Available here: https://www.codewars.com/kata/5663f5305102699bad000056
"""


# solution
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    len_a1 = len(a1)
    len_a2 = len(a2)
    longer_arr = (a1 if len_a1 > len_a2 else a2)
    shorter_arr = (a1 if len_a1 < len_a2 else a2)
    max_len = abs(len(longer_arr[0]) - len(shorter_arr[0]))

    if len_a1 != len_a2:
        for j in range(len(longer_arr)):
            i = 0
            while i < len(shorter_arr):
                current_len = abs(len(longer_arr[j])
                                  - len(shorter_arr[i]))
                if current_len > max_len:
                    max_len = current_len
                i += 1
    else:
        for j in range(len_a1):
            i = 0
            while i < len(a2):
                current_len = abs(len(a1[j]) - len(a2[i]))
                i += 1
                if current_len > max_len:
                    max_len = current_len

    return max_len


# Example
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
