import numpy as np

# Taking user input for the number of variables
n = int(input("Enter the number of variables: "))

# Taking user input for matrix A
print(f"Enter the values for matrix A ({n}x{n}):")
A = np.zeros((n, n))
for i in range(n):
    row = input(f"Enter the values for row {i+1} (space-separated): ")
    A[i] = list(map(int, row.split()))

# Taking user input for vector y
print(f"Enter the values for vector y (1x{n}):")
y = input("Enter the values (space-separated): ")
y = np.array(list(map(int, y.split())))

# Solving the system of linear equations
x = np.linalg.solve(A, y)
print("Solution:")
print(x)
