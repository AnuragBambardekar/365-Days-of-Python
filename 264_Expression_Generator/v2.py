"""
Expression Evaluator with Timing

The program now includes timing information, displaying how long it took to find the solutions. 
This is useful for assessing the efficiency of the expression evaluation process.
"""

import itertools
import math
import time

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
    
    solutions = []

    start_time = time.time()

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

            if math.isclose(result, target, rel_tol=1e-9):
                solutions.append(expression)

    end_time = time.time()

    return solutions, end_time - start_time

if __name__ == "__main__":
    input_numbers = input("Enter some numbers separated by spaces: ")
    target_number = int(input("Enter the target number: "))

    numbers = [int(num) for num in input_numbers.split()]
    operator_symbol = {OP_ADD: "+", OP_SUB: "-", OP_MUL: "*", OP_DIV: "/"}

    solutions, elapsed_time = evaluate_expression(numbers, operators, target_number)

    print(f"Target is {target_number}")
    print("--------------------")

    for solution in solutions:
        print(solution)

    print(f"{len(solutions)} solution(s) in {elapsed_time:.3f} seconds")
    print(f"{len(numbers)} duplication(s)")
    print(f"{len(set(itertools.permutations(numbers)))} combination(s)")
