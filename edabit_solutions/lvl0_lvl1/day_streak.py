def daily_streak(lst):
    streaks = []
    streak = 0
    for day in lst:
        if day:
            streak += 1
        else:
            streaks.append(streak)
            streak = 0
    streaks.append(streak)
    return max(streaks)


if __name__ == '__main__':
    daily_streak([True, False, True, True]), 2
