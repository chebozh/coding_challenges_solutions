"""Current Streak

Create a function that takes the current day (e.g. "2019-09-30"),
a list of date dictionaries and returns the "current streak" (i.e. number of consecutive days in a row).
Examples

current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]) ➞ 3

current_streak("2019-09-25", [
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]) ➞ 0

    The list of dates is sorted chronologically.
    The today parameter will always be greater than or equal to the last date in the list.
    An empty list should return 0.
"""


# solution
def current_streak(today, lst):
    if not lst or lst[len(lst)-1]['date'] != today:
        return 0

    streak = 0
    for i in range(len(lst)-1):
        curr_day = lst[i]['date'][-2:]
        next_day = lst[i+1]['date'][-2:]
        if abs(int(curr_day) - int(next_day)) == 1:
            streak += 1
        else:
            streak = 0
    return streak + 1


if __name__ == '__main__':
    assert current_streak("2019-09-23", [
        {
            "date": "2019-09-18"
        },
        {
            "date": "2019-09-19"
        },
        {
            "date": "2019-09-21"
        },
        {
            "date": "2019-09-22"
        },
        {
            "date": "2019-09-23"
        }
    ]) == 3

    assert current_streak("2019-09-25", [
        {
            "date": "2019-09-16"
        },
        {
            "date": "2019-09-17"
        },
        {
            "date": "2019-09-21"
        },
        {
            "date": "2019-09-22"
        },
        {
            "date": "2019-09-23"
        }
    ]) == 0
