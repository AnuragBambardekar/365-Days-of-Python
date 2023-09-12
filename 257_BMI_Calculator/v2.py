def calculate_bmi(weight, height):
    height_meters = height / 100.0
    bmi = weight / (height_meters * height_meters)
    
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        
        bmi = calculate_bmi(weight, height)
        
        print(f"Your BMI is {bmi:.2f}")
        category = categorize_bmi(bmi)
        print(f"You are categorized as: {category}")
    except ValueError:
        print("Invalid input. Please enter valid numerical values for weight and height.")
