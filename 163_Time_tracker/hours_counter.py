total_minutes_worked = 0

while True:
    a = input("Enter hours and minutes (or 'q' to stop entering): ")
    if a == 'q':
        break
    
    try:
        hours, minutes = map(int, a.split())
        total_minutes_worked += hours * 60 + minutes
    except ValueError:
        print("Invalid input. Please enter hours and minutes in the correct format.")

# print("Total number of hours entered:", total_hours)

total_hours = total_minutes_worked // 60
remaining_minutes = total_minutes_worked % 60

print("Total time entered: {} hours and {} minutes".format(total_hours, remaining_minutes))

work_hours_input = input("Enter the number of hours you are supposed to work: ")
total_work_minutes = 0
try:
    work_hours, work_minutes = map(int, work_hours_input.split())
    total_work_minutes += work_hours * 60 + work_minutes
except ValueError:
    print("Invalid input. Please enter hours and minutes in the correct format.")

# print(total_minutes_worked)
# print(total_work_minutes)

remaining_minutes_to_work = total_work_minutes - total_minutes_worked

# print(remaining_minutes_to_work)

rem_hours = remaining_minutes_to_work // 60
rem_minutes = remaining_minutes_to_work % 60

print("Remaining time you can work: {} hours and {} minutes".format(rem_hours, rem_minutes))