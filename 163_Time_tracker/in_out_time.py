in_time_input = input("Enter the in time in hours and minutes (e.g., 9 30 for 9:30 AM): ")
num_hours_input = input("Enter the number of hours to work: ")

try:
    in_hours, in_minutes = map(int, in_time_input.split())
    num_hours, num_minutes = map(int, num_hours_input.split())

    out_minutes = (in_hours * 60 + in_minutes) + num_hours * 60 + num_minutes
    out_hours = (out_minutes // 60) % 24
    out_minutes = out_minutes % 60
    print("Out time: {}:{:02d}".format(out_hours, out_minutes))
except ValueError:
    print("Invalid input. Please enter the in time in the correct format.")