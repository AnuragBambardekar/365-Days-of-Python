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

# Get the current local time
current_local_time = datetime.datetime.now()

# Print the current local time
print("Current local time:", current_local_time)

# Define your local timezone
local_timezone = 'America/New_York'

# Retrieve the available time zones
available_timezones = pytz.all_timezones

# Display the available time zones
print("Available time zones:")
for i, tz in enumerate(available_timezones, start=1):
    print("{}. {}".format(i, tz))

# Ask the user to choose a time zone
selected_timezone_index = int(input("Enter the number corresponding to the desired time zone: "))
selected_timezone = available_timezones[selected_timezone_index - 1]

print(selected_timezone)

# Convert to UTC
utc_time = convert_to_utc(current_local_time, local_timezone)
print("Converted time (UTC):", utc_time)

# Convert to selected_timezone
ist_time = convert_to_timezone(utc_time, selected_timezone)
print("Converted time:", ist_time)
