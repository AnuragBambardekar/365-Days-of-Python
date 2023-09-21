import itertools
import math

# Operators
OP_ADD = 1  # Addition
OP_SUB = 2  # Subtraction
OP_MUL = 3  # Multiplication
OP_DIV = 4  # Division

# List of basic operators
operators = [OP_ADD, OP_SUB, OP_MUL, OP_DIV]

def evaluate_expression(numbers, operators, target):
    # Generate all permutations of the numbers
    number_permutations = itertools.permutations(numbers)

    # Try all possible combinations of numbers and operators
    for num_permutation in number_permutations:
        for op_permutation in itertools.product(operators, repeat=len(numbers) - 1):
            expression = str(num_permutation[0])
            result = num_permutation[0]

            for i, num in enumerate(num_permutation[1:], start=1):
                op = op_permutation[i - 1]
                expression += f" {operator_symbol[op]} {num}"
                if op == OP_ADD:
                    result += num
                elif op == OP_SUB:
                    result -= num
                elif op == OP_MUL:
                    result *= num
                elif op == OP_DIV:
                    if num == 0:
                        continue  # Avoid division by zero
                    result /= num

            if result == target:
                print(f"{target} = {expression}")

if __name__ == "__main__":
    input_numbers = input("Enter some numbers separated by spaces: ")
    target_number = int(input("Enter the target number: "))

    numbers = [int(num) for num in input_numbers.split()]
    operator_symbol = {OP_ADD: "+", OP_SUB: "-", OP_MUL: "*", OP_DIV: "/"}

    evaluate_expression(numbers, operators, target_number)




# 4 - ((6 - 8) * 10)
# 4 + ((8 - 6) * 10)
# (4 * (10 - 6)) + 8
# ((8 - 6) * 10) + 4
# 8 - ((6 - 10) * 4)
# 8 + ((10 - 6) * 4)
# ((10 - 6) * 4) + 8
# (10 * (8 - 6)) + 4
