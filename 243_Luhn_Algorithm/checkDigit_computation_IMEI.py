import pretty_errors, math

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_num = input("Enter an IMEI # without the check digit: ") # 15-digit number 49-015420-323751-8 where '8' is the check digit.

# remove - and ' '
card_num_copy = card_num.replace("-","")
card_num_copy = card_num_copy.replace(" ","")
# card_num_copy = card_num_copy[:-1] # because we are accepting IMEI without the check digit
card_num_copy = card_num_copy + '0'
# print(card_num_copy)

# summing the digits from right to left
card_num_copy = card_num_copy[::-1]
for x in card_num_copy[::2]:
    sum_odd_digits += int(x)

# print(sum_odd_digits)

# double every second digit from right to left
for x in card_num_copy[1::2]:
    x = int(x) * 2
    if x >= 10:
        # split and add the number
        sum_even_digits += (1 + ( x % 10 ))
    else:
        sum_even_digits += x

# add the sum of odd digits & sum of even digits
total = sum_odd_digits + sum_even_digits
# print(total)

if (total % 10) != 0:
    ceil_val = math.ceil(total / 10) * 10
    difference = ceil_val - total

print(f"Check Digit is: {difference}")
print(f"IMEI is: {card_num}-{difference}")