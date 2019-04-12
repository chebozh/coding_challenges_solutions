"""
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water",
"Fish", and "Sun" appear without overlapping (regardless of the case).

Examples

sum_of_a_beach("WAtErSlIde")                    ==>  1
sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
sum_of_a_beach("cItYTowNcARShoW")               ==>  0

"""
# solution
import re


def sum_of_a_beach(beach):
    res = []
    word_set = ("sand", "water", "fish", "sun")
    beach_lower = beach.lower()

    for w in word_set:
        res += re.findall(w, beach_lower)
    return len(res)


# Examples
print(sum_of_a_beach("SanD"))  # 1
print(sum_of_a_beach("sunshine"))  # 1
print(sum_of_a_beach("sunsunsunsun"))  # 4
print(sum_of_a_beach("123FISH321"))  # 1
