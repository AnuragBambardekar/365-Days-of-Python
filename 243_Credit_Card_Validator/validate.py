sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_num = input("Enter a credit card #: ")

# remove - and ' '
card_num = card_num.replace("-","")
card_num = card_num.replace(" ","")

# summing the digits from right to left
card_num = card_num[::-1]
for x in card_num[::2]:
    sum_odd_digits += int(x)

# double every second digit from right to left
for x in card_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        # split and add the number
        sum_even_digits += (1 + ( x % 10 ))
    else:
        sum_even_digits += x

# add the sum of odd digits & sum of even digits
total = sum_odd_digits + sum_even_digits

# if total is divisible by 10, then valid
if (total % 10) == 0:
    print("VALID")
else:
    print("INVALID")

"""
Test Credit Card Account Numbers
American Express 378282246310005
American Express 371449635398431
American Express Corporate 378734493671000
Australian Bankcard 5610591081018250
Diners Club 30569309025904
Diners Club 38520000023237
Discover 6011111111111117
Discover 6011000990139424
JCB 3530111333300000
JCB 3566002020360505
MasterCard 5555555555554444
MasterCard 5105105105105100
Visa 4111111111111111
Visa 4012888888881881
"""