"""###Instructions

Write a function that takes a negative or positive integer, which represents the number of minutes before (-) or after
(+) Sunday midnight, and returns the current day of the week and the current time in 24hr format ('hh:mm') as a string.

day_and_time(0)       should return 'Sunday 00:00'
day_and_time(-3)      should return 'Saturday 23:57'
day_and_time(45)      should return 'Sunday 00:45'
day_and_time(759)     should return 'Sunday 12:39'
day_and_time(1236)    should return 'Sunday 20:36'
day_and_time(1447)    should return 'Monday 00:07'
day_and_time(7832)    should return 'Friday 10:32'
day_and_time(18876)   should return 'Saturday 02:36'
day_and_time(259180)  should return 'Thursday 23:40'
day_and_time(-349000) should return 'Tuesday 15:20'
"""
# solution
import datetime
import calendar


def day_and_time(mins):
    start = datetime.datetime(2018, 10, 7, 00, 00)
    new_time = start + datetime.timedelta(minutes=mins)
    weekday = calendar.day_name[new_time.weekday()]

    return '{} {}'.format(weekday, new_time.time())[:-3]


# examples
print(day_and_time(0))
print(day_and_time(-349000))
print(day_and_time(7832))
