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

def convert_to_ist(utc_time):
    # Create a timezone object for Indian Standard Time (IST)
    ist_tz = pytz.timezone('Asia/Kolkata')
    
    # Convert the UTC datetime to IST
    ist_dt = utc_time.astimezone(ist_tz)
    
    return ist_dt

# Get the current local time
current_local_time = datetime.datetime.now()

# Print the current local time
print("Current local time:", current_local_time)

# Define your local timezone
local_timezone = 'America/New_York'

# Convert to UTC
utc_time = convert_to_utc(current_local_time, local_timezone)
print("Converted time (UTC):", utc_time)

# Convert to Indian Standard Time (IST)
ist_time = convert_to_ist(utc_time)
print("Converted time (IST):", ist_time)
