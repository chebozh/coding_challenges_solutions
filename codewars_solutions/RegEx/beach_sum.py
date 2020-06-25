"""
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear without overlapping (regardless of the case).
Examples

sum_of_a_beach("WAtErSlIde")                    ==>  1
sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
sum_of_a_beach("cItYTowNcARShoW")               ==>  0

7kuy
"""
# solution
import re


def sum_of_a_beach(beach):
    return len(re.findall(r'sand|water|fish|sun', beach, re.IGNORECASE))

# examples
print(sum_of_a_beach("WAtErSlIde"))
print(sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"))
print(sum_of_a_beach("gOfIshsunesunFiSh"))
print(sum_of_a_beach("cItYTowNcARShoW"))
