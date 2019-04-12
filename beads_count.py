"""
Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below
work out the number of red beads.

@ @@ @ @@ @ @@ @ @@ @ @@ @

Implement count_red_beads(N_blue) (in PHP count_red_beads($n); in Java, Javascript countRedBeads(n)) so that it returns
the number of red beads.
If there are less than 2 blue beads return 0.

Available at: https://www.codewars.com/kata/simple-beads-count/train/python
"""


# solution
def count_red_beads(N_blue):
    if N_blue == 1 or N_blue == 0:
        return 0
    magic_number = (1 - N_blue) * -1
    return magic_number * 2


# Examples
print(count_red_beads(1))
print(count_red_beads(3))
print(count_red_beads(5))
