import math

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the equation has real roots
    if discriminant >= 0:
        # Calculate the two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        # If the discriminant is negative, the equation has complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

roots = solve_quadratic_equation(a, b, c)
print("The roots are:", roots)
