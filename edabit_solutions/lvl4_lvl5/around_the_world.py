"""Time Around the World

In this challenge, the goal is to calculate what time it is in two different cities.
You're given a string city_a and the related string timestamp (time in city_a) with the date formatted in full U.S.
notation, as in this example:

"July 21, 1983 23:01"

You have to return a new timestamp with date and corresponding time in city_b, formatted as in this example:

"1983-7-22 23:01"

See the table below for a list of given cities and their GMT (Greenwich Mean Time) hours offsets.
GMT	City
- 08:00	Los Angeles
- 05:00	New York
- 04:30	Caracas
- 03:00	Buenos Aires
00:00	London
+ 01:00	Rome
+ 03:00	Moscow
+ 03:30	Tehran
+ 05:30	New Delhi
+ 08:00	Beijing
+ 10:00	Canberra
Examples

time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") ➞ "2011-4-2 17:23"
# Can be a new day.

time_difference("London", "July 31, 1983 23:01", "Rome") ➞ "1983-8-1 00:01"
# Can be a new month.

time_difference("New York", "December 31, 1970 13:40", "Beijing") ➞ "1971-1-1 02:40"
# Can be a new year.

Notes

    Pay attention to hours and minutes, a leading 0 is needed in the returned timestamp when they're a single digit.
    Pay attention to cities with half hours offsets.
"""
from datetime import datetime, timedelta


def time_difference(city_a, timestamp, city_b):
    conversion_table = {
        'Los Angeles': -8,
        'New York': -5,
        'Caracas': -4.5,
        'Buenos Aires': -3,
        'London': 0,
        'Rome': 1,
        'Moscow': 3,
        'Tehran': 3.5,
        'New Delhi': 5.5,
        'Beijing': 8,
        'Canberra': 10
    }
    cities_time_difference = conversion_table[city_b] - conversion_table[city_a]
    city_a_td = datetime.strptime(timestamp, '%B %d, %Y %H:%M')
    city_b_td = city_a_td + timedelta(hours=cities_time_difference)
    return city_b_td.strftime('%Y-%-m-%-d %H:%M')


if __name__ == '__main__':
    assert time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") == "2011-4-2 17:23"
    # Can be a new day.

    assert time_difference("London", "July 31, 1983 23:01", "Rome") == "1983-8-1 00:01"
    # Can be a new month.

    assert time_difference("New York", "December 31, 1970 13:40", "Beijing") == "1971-1-1 02:40"
    # Can be a new year.
