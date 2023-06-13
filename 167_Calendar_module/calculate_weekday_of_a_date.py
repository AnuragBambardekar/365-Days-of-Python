import calendar

def get_weekday(year, month, day):
    weekday = calendar.weekday(year, month, day)
    return calendar.day_name[weekday]

year = 2023
month = 6
day = 13
weekday = get_weekday(year, month, day)
print(weekday)
