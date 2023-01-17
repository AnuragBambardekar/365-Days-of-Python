from functools import lru_cache

@lru_cache(maxsize=1000)

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

# Initialize a counter to keep track of how many Armstrong numbers we've found
count = 0
# Initialize a number to start checking at
num = 1

# Keep looping until we've found 100 Armstrong numbers
while count < 50:
    # Check if the number is an Armstrong number
    if is_armstrong(num):
        # If it is, print it and increment the counter
        print(num)
        count += 1
    # Increment the number to check the next one
    num += 1