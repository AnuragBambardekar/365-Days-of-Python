def zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

def main():
    try:
        day = int(input("Enter the day of your birth (1-31): "))
        month = int(input("Enter the month of your birth (1-12): "))
        
        if (day < 1 or day > 31) or (month < 1 or month > 12):
            print("Invalid input. Please enter a valid day and month.")
        else:
            sign = zodiac_sign(day, month)
            print(f"Your zodiac sign is {sign}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for day and month.")

if __name__ == "__main__":
    main()
