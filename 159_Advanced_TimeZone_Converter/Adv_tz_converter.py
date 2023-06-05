import datetime
import pytz

def convert_to_utc(local_time, local_timezone):
    # Create a timezone object for the local timezone
    local_tz = pytz.timezone(local_timezone)
    
    # Localize the input datetime with the local timezone
    local_dt = local_tz.localize(local_time)
    
    # Convert the datetime to UTC
    utc_dt = local_dt.astimezone(pytz.UTC)
    
    return utc_dt

def convert_to_timezone(utc_time, selected_timezone):
    # Create a timezone object for selected timezone
    tz = pytz.timezone(selected_timezone)
    
    # Convert the UTC datetime to IST
    dt = utc_time.astimezone(tz)
    
    return dt

# Retrieve the available time zones
available_timezones = pytz.all_timezones

# Display the available time zones
print("Available time zones:")
for i, tz in enumerate(available_timezones, start=1):
    print("{}. {}".format(i, tz))

# Ask the user to choose a time zone
selected_timezone_index1 = int(input("Enter the number corresponding to the time zone in which you are: "))
selected_timezone = available_timezones[selected_timezone_index1 - 1]

time_str = input('Enter a time and date in the format MM/DD/YYYY HH:MM: ')
time_str = datetime.datetime.strptime(time_str, '%m/%d/%Y %H:%M')

# Ask the user to choose a time zone
selected_timezone_index2 = int(input("Enter the number corresponding to the desired time zone which you want to convert to: "))
selected_timezone_to_convert = available_timezones[selected_timezone_index2 - 1]


# Print the selected TimeZones
print("Timezone Selected: ", selected_timezone)
print("Converting to Timezone: ",selected_timezone_to_convert)

# Convert to UTC
utc_time = convert_to_utc(time_str, selected_timezone)
print("Converting time to UTC:", utc_time)

# Convert to selected_timezone
time = convert_to_timezone(utc_time, selected_timezone_to_convert)
print("Converted time:", time)
