import numpy as np

def solve_cubic_equation(a, b, c, d):
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    return roots

a = float(input("Enter the coefficient of x^3: "))
b = float(input("Enter the coefficient of x^2: "))
c = float(input("Enter the coefficient of x: "))
d = float(input("Enter the constant term: "))

solutions = solve_cubic_equation(a, b, c, d)
print("The solutions are:", solutions)
