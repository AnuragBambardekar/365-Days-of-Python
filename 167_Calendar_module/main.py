"""
The calendar module allows us to output calendars like the program and provides additional useful functions related to the calendar. 
Functions and classes defined in the calendar module use an idealized calendar, the current Gregorian calendar extended indefinitely 
in both directions.
"""

import calendar
   
yy = 2023
mm = 10
   
# display the calendar
print(calendar.month(yy, mm))

print ("The calendar of year 2023 is : ")
print (calendar.calendar(2023))