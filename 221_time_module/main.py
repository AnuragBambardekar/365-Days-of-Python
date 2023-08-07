import time

# convert a time expressed in seconds since epoch to a readable string
# epoch = when your computer thinks time began (reference point)
print(time.ctime(0)) # Wed Dec 31 19:00:00 1969

print(time.ctime(1000000)) # 1 million seconds after epoch

print(time.time()) # return current seconds since epoch (in seconds)

print(time.ctime(time.time())) # returns current date and time

time_obj = time.localtime()
print(time_obj) # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=7, tm_hour=10, tm_min=57, tm_sec=14, tm_wday=0, tm_yday=219, tm_isdst=1)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_obj)
print(local_time)

# Get the UTC Time
time_obj = time.gmtime()
# print(time_obj)

time_string = "20 April, 2023"
time_obj = time.strptime(time_string, "%d %B, %Y")
print(time_obj)

time_tuple = (2023, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_string = time.mktime(time_tuple) # in seconds
print(time_string)