"""Find the Lost Dog

    0 represents the dog.
    Each list represents a house and each 1 represents an empty room.
    Return the house and the room where it is located, there can be only one dog lost per building.

Examples

lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ "Dog not found!"

lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}

lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)",
 "Dog4": "House (4) and Room (3)"}
"""


def lost_dog(*houses):
    dog_n = 0
    found = {}

    for house_n, house in enumerate(houses, start=1):
        for room_n, room in enumerate(house, start=1):
            if room == 0:
                dog_n += 1 # A doggo!
                found[f'Dog{dog_n}'] = f'House ({house_n}) and Room ({room_n})'

    return found or 'Dog not found!'


if __name__ == '__main__':
    assert lost_dog([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) == "Dog not found!"

    assert lost_dog([1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) == {
        "Dog1": "House (2) and Room (1)",
        "Dog2": "House (3) and Room (2)"}

    assert lost_dog([1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1]) == {
        "Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)",
        "Dog4": "House (4) and Room (3)"}
