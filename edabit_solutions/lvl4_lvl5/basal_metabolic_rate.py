"""
Basal Metabolic Rate

Create a function that takes a dict with the size, the weight in kg, the age, how much sport the person does and whether
 the person is male or female:

dict = {
  "gender": "male",
  "height": 180,
  "weight": 80,
  "age": 20,
  "sport": 3
}

Return the basal metabolic rate of the person rounded to one decimal place. The formula is:

    BMR for Men: 66.47 + (13.75 weight) + (5.003 height) − (6.755 * age)
    BMR for Women: 655.1 + (9.563 weight) + (1.85 height) − (4.676 * age)

Once you’ve calculated your BMR, this is then put into the Harris Benedict Formula , which calculates your total calorie
 intake required to maintain your current weight. This is as follows:

    Little/no exercise(1): BMR * 1.2 = Total Calorie Need
    Light exercise(2): BMR * 1.375 = Total Calorie Need
    Moderate exercise (3): BMR * 1.55 = Total Calorie Need
    Very active (4): BMR * 1.725 = Total Calorie Need
    Extra active (5): BMR * 1.9 = Total Calorie Need

Examples

BMR({
  "gender": "female",
  "height": 170,
  "weight": 65,
  "age": 25,
  "sport": 5
}) ➞ 2801.2


BMR({
  "gender": "male",
  "height": 180,
  "weight": 80,
  "age": 20,
  "sport": 3
}) ➞ 2994.5


BMR({
  "gender": "female",
  "height": 170,
  "weight": 70,
  "age": 40,
  "sport": 2
}) ➞ 1996.5
"""


def BMR(person):
    weight = person['weight']
    height = person['height']
    age = person['age']
    exercise = person['sport']
    calorie_intake_per_exercise = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }

    if person['gender'] == 'male':
        bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

    return round(calorie_intake_per_exercise[exercise] * bmr, 1)


if __name__ == '__main__':
    assert BMR({
        "gender": "female",
        "height": 170,
        "weight": 65,
        "age": 25,
        "sport": 5
    }) == 2801.2

    assert BMR({
        "gender": "male",
        "height": 180,
        "weight": 80,
        "age": 20,
        "sport": 3
    }) == 2994.5

    assert BMR({
        "gender": "female",
        "height": 170,
        "weight": 70,
        "age": 40,
        "sport": 2
    }) == 1996.5

    print(BMR({
        "gender": "male",
        "height": 178,
        "weight": 60,
        "age": 29,
        "sport": 3
    }))
