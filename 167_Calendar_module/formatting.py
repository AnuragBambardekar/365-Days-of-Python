import calendar

# Create an instance of the calendar
cal = calendar.Calendar()

# Get the current year and month
current_year = 2023
current_month = 6

# Generate the month's calendar
month_calendar = cal.monthdayscalendar(current_year, current_month)

# Define color codes
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Define weekdays and their corresponding color codes
weekday_colors = {
    0: RED,   # Monday
    1: RED,   # Tuesday
    2: RED,   # Wednesday
    3: RED,   # Thursday
    4: RED,   # Friday
    5: GREEN, # Saturday
    6: GREEN  # Sunday
}

# Print the calendar header
print(f"{current_month}/{current_year}")
print("Mo Tu We Th Fr Sa Su")

# Print the calendar
for week in month_calendar:
    for day in week:
        if day == 0:
            # Empty day
            print('  ', end=' ')
        else:
            # Get the weekday of the current day
            weekday = calendar.weekday(current_year, current_month, day)
            # Get the color code for the weekday
            color_code = weekday_colors[weekday]
            # Print the day with the corresponding color
            print(f'{color_code}{day:2}{RESET}', end=' ')
    print()
