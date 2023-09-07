import arrow

print("UTC Time: ",arrow.utcnow()) #UTC
print("Unix Time: ",arrow.utcnow().timestamp()) #Unix Time
print("Year: ",arrow.utcnow().year) 
print("Month: ",arrow.utcnow().month) 
print("Day: ",arrow.utcnow().day) 
print("Date Format: ",arrow.utcnow().format('MM/DD/YYYY')) 

print("Time Format: ",arrow.utcnow().format('hh:mm:ss a ZZ')) 
print("Time Format: ",arrow.now('US/Eastern').format('hh:mm:ss a ZZ')) 

# Time Travel
now = arrow.now()
past = now.shift(hours=-1)
print("An hour ago, the time was: ", past.format('hh:mm:ss a ZZ'))

# Humanize
print("An hour ago, the time was: ", past.humanize())

#Humanize to past
apast = arrow.utcnow().shift(hours=-1)
print(apast.humanize())
 
#humanize to future
present = arrow.utcnow()
afuture = present.shift(hours=3)
print(afuture.humanize(present))
 
#Indicate a specific time granularity
afuture = present.shift(minutes=73)
print(afuture.humanize(present, granularity="minute"))
print(afuture.humanize(present, granularity=["hour", "minute"]))

# Get the Unix Timestamp (when it starts)
occasion = arrow.get(0)
print("Unix Timestamp: ",occasion.format('MMMM D YYYY'))

occasion = arrow.get(12345678901234567)
print("Unix Timestamp: ",occasion.format('MMMM D YYYY'))

# Parse/Search from/in String
bday = arrow.get('My Birthday is on: 1998-08-10', 'YYYY-DD-MM')
print("Parsing Birthday from a string: ",bday.format('MMMM D YYYY'))

# Iterate over time (ranges)
now = arrow.now()
future  = now.shift(hours=5)

for each in arrow.Arrow.range('hour', now, future):
    print(each.format('dddd h:mm a')) # d = 4, ddd = Thu, dddd = Thursday

