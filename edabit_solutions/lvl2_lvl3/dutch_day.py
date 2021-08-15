"""The Day in Dutch

Write a method that when passed a date as "dd mm yyyy" and returns the date's weekday name in the Dutch culture.
Examples

weekday_dutch("21 9 1970") ➞ "maandag"

weekday_dutch("2 9 1945") ➞ "zondag"

weekday_dutch("9 11 2001") ➞ "dinsdag"

Notes

    Check the Resources tab for help.
    You can assume the specified date is valid.
"""
import calendar

import datetime


def weekday_dutch(date):
    dutch_days = {
        'Monday': 'maandag',
        'Tuesday': 'dinsdag',
        'Wednesday': 'woensdag',
        'Thursday': 'donderdag',
        'Friday': 'vrijdag',
        'Saturday': 'zaterdag',
        'Sunday': 'zondag',
    }
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return dutch_days[calendar.day_name[day]]


if __name__ == '__main__':
    assert weekday_dutch("10 12 2050") == "zaterdag"
    assert weekday_dutch("14 10 6010") == "donderdag"
    assert weekday_dutch("31 1 1000") == "vrijdag"
