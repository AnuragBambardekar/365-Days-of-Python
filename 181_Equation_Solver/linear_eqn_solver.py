def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        x = -b / a
        return x

a = float(input("Enter the coefficient of x: "))
b = float(input("Enter the constant term: "))

solution = solve_linear_equation(a, b)
print("The solution is:", solution)
