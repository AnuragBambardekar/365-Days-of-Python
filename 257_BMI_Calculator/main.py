import math

def getWeight():
    weight = float(input("Please enter your weight in pounds: "))
    return weight

def getHeight():
    height = input("Please enter your height in feet and inches (ex: 5'8\"): ")
    splitString = height.split("'")
    feet = float(splitString[0])
    inches = float(splitString[1].strip('"'))
    height = (feet * 12) + inches
    return height

def calculateBMI(weight, height):
    meters = height * 0.0254
    kilograms = weight * 0.453592
    bmi = kilograms / (meters * meters)
    return bmi

if __name__ == "__main__":
    print("Welcome to the BMI Calculator!")

    weight = getWeight()
    height = getHeight()

    bmi = calculateBMI(weight, height)
    print(f"Your final BMI is: {round(bmi,2)}")