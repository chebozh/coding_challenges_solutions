"""
To Adjust the Time

In this challenge, you have to add a variable amount of hours, minutes and seconds to a given time, obtaining, in turn,
a new adjusted time.

Given a string now being a timestamp in the format hh:mm:ss, and three integers hrs, mins and sec being the hours,
minutes and seconds to add, implement a function that returns a string being the newly adjusted timestamp
(maintaining the same format).

Examples

time_adjust("01:00:00", 1, 30, 10) ➞ "02:30:10"

time_adjust("18:22:30", 4, 60, 30) ➞ "23:23:00"

time_adjust("00:00:00", 72, 120, 120) ➞ "02:02:00"

Notes

    The amounts of hrs, mins and sec can be any positive integer, and you have to correctly add them to the
    corresponding unit if they exceed their scale. See example #2: sixty minutes is one hour, and sixty seconds
    (30 + 30) is one minute.
    If the amount of time to add exceeds the 24 hours, then the time will start again from "00:00:00".
    See example #3: 72 hours are 3 exact days so that after three cycles of 24 hours, the hour will be again "00"
    (and becomes "02" because we are adding also 120 minutes or 2 hours).
"""
from datetime import datetime, timedelta


def time_adjust(now, hrs, mins, sec):
    fixed_hour, fixed_min, fixed_sec = map(int, now.split(':'))
    fixed_now = datetime.today().replace(hour=fixed_hour, minute=fixed_min, second=fixed_sec)
    adjusted_now = fixed_now + timedelta(hours=hrs, minutes=mins, seconds=sec)
    return adjusted_now.strftime("%H:%M:%S")


if __name__ == '__main__':
    assert time_adjust("01:00:00", 1, 30, 10) == "02:30:10"

    assert time_adjust("18:22:30", 4, 60, 30) == "23:23:00"

    assert time_adjust("00:00:00", 72, 120, 120) == "02:02:00"
