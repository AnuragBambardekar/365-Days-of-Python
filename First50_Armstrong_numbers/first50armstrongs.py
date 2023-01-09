def is_armstrong(num):
    # Convert the number to a string so we can iterate through its digits
    num_str = str(num)
    # Initialize a sum to keep track of the sum of the digits
    sum = 0
    # Iterate through the digits of the number
    for digit in num_str:
        # Raise the digit to the power of the number of digits and add it to the sum
        sum += int(digit)**len(num_str)
    # Return True if the sum is equal to the original number, False otherwise
    if(sum==num):
        res = num
        return res

