"""
Premier League Champions

Create a function that takes a list of football clubs with properties: name, wins, loss, draws, scored, conceded,
and returns the team name with the highest number of points. If two teams have the same number of points,
return the team with the largest goal difference.

How to Calculate Points and Goal Difference

team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68

Examples

champions([
  {
    "name": "Manchester United",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 88,
    "conceded": 20,
  },
  {
    "name": "Arsenal",
    "wins": 24,
    "loss": 6,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  },
  {
    "name": "Chelsea",
    "wins": 22,
    "loss": 8,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  }
]) ➞ "Manchester United"

Notes

Input is a list of teams.
"""


def champions(teams: dict):
    champ = max(teams, key=lambda t: (3 * t['wins'] + 0 * t['loss'] + 1 * t['draws'],
                                      t['scored'] - t['conceded']))
    return champ['name']


if __name__ == '__main__':
    print(champions([
        {
            "name": "Manchester United",
            "wins": 30,
            "loss": 3,
            "draws": 5,
            "scored": 88,
            "conceded": 20,
        },
        {
            "name": "Arsenal",
            "wins": 24,
            "loss": 6,
            "draws": 8,
            "scored": 98,
            "conceded": 29,
        },
        {
            "name": "Chelsea",
            "wins": 22,
            "loss": 8,
            "draws": 8,
            "scored": 98,
            "conceded": 29,
        }
    ]))
