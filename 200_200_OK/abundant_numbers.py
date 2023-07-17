def find_abundant_numbers(start, end):
    abundant_numbers = []
    
    for num in range(start, end + 1):
        divisor_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)
        if divisor_sum > num:
            abundant_numbers.append(num)
    
    return abundant_numbers


start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

result = find_abundant_numbers(start_range, end_range)
print("Abundant numbers within the range:", result)
