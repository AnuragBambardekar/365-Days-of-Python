import calendar

def find_leap_years(start_year, end_year):
    leap_years = []
    for year in range(start_year, end_year + 1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

start_year = 2000
end_year = 2025
leap_years = find_leap_years(start_year, end_year)
print(leap_years)
