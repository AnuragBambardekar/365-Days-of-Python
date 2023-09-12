def feet_and_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    # 1 inch = 2.54 cm
    cm = total_inches * 2.54
    return cm

try:
    feet = float(input("Enter feet: "))
    inches = float(input("Enter inches: "))
    centimeters = feet_and_inches_to_cm(feet, inches)
    print(f"{feet} feet and {inches} inches is equal to {centimeters:.2f} cm")
except ValueError:
    print("Invalid input. Please enter valid numerical values for feet and inches.")
