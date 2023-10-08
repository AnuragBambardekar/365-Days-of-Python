import datetime, random

def getBirthdays(noOfBirthdays):
    birthdays = []
    for i in range(noOfBirthdays):
        startOfYear = datetime.date(2023,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    # print(birthdays)
    return birthdays

# print(getBirthdays(5))

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # all birthdays are unique
    
    for a, i in enumerate(birthdays):
        for b, j in enumerate(birthdays[a+1: ]):
            if i == j:
                return i # return matching birthday

MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
          'Nov','Dec')

while True:
    print("How many birthdays to generate? (max=100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print(numBDays, "Birthdays: ")
birthdays = getBirthdays(numBDays)
for i, b in enumerate(birthdays):
    if i!=0:
        print(', ', end='')
    monthName = MONTHS[b.month - 1]
    dateText = '{} {}'.format(monthName, b.day)
    print(dateText, end='')
print("\n")

# determine if 2 birthdays match
match = getMatch(birthdays)
print("In this simulation: ")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Multiple people have a birthday on: ',dateText)
else:
    print("No Matching Birthdays!")
print("\n")

# Run through 10000 simulations
print('Generating ',numBDays, 'random birthdays 10000 times...')
input("Enter to Begin...")

simMatch = 0 # how many simulations had matching birthdays in them
for i in range(10000):
    if i%1000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print("Done running 10000 simulations!")

# display results
probability = round(simMatch / 10000 * 100, 2)
print("Out of",numBDays,"people the probability of 2 people having birthday on same day is: ", probability)

