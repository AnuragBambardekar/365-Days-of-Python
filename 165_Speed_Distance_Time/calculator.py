def calculate_speed(distance, time):
    speed = distance / time
    return speed

def calculate_distance(speed, time):
    distance = speed * time
    return distance

def calculate_time(distance, speed):
    time = distance / speed
    return time

def format_time(time):
    hours = int(time)
    minutes = int((time * 60) % 60)
    seconds = int((time * 3600) % 60)
    return hours, minutes, seconds

def main():
    print("Welcome to the Speed-Distance Calculator!")
    print("1. Calculate Speed")
    print("2. Calculate Distance")
    print("3. Calculate Time")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        distance = float(input("Enter the distance: "))
        time = float(input("Enter the time: "))

        distance_unit = input("Enter the unit for distance (km/miles): ")
        time_unit = input("Enter the unit for time (hours/minutes): ")

        if distance_unit.lower() == "miles":
            distance *= 1.60934

        if time_unit.lower() == "minutes":
            time /= 60

        speed = calculate_speed(distance, time)

        print(f"The speed is {speed} km/h.")
    elif choice == 2:
        speed = float(input("Enter the speed: "))
        speed_unit = input("Enter the unit for speed (kmph/mph): ")
        time = float(input("Enter the time: "))

        if speed_unit.lower() == "mph":
            speed *= 1.60934

        time_unit = input("Enter the unit for time (hours/minutes): ")

        if time_unit.lower() == "minutes":
            time /= 60

        distance = calculate_distance(speed, time)
        print(f"The distance is {distance} km.")
    elif choice == 3:
        distance = float(input("Enter the distance: "))
        speed = float(input("Enter the speed: "))

        distance_unit = input("Enter the unit for distance (km/miles): ")
        speed_unit = input("Enter the unit for speed (kmph/mph): ")
        if speed_unit.lower() == "mph":
            speed *= 1.60934

        if distance_unit.lower() == "miles":
            distance *= 1.60934

        time = calculate_time(distance, speed)
        hours, minutes, seconds = format_time(time)

        print(f"The time is {hours} hours, {minutes} minutes, and {seconds} seconds.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
