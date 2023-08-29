# Luhn Checksum Algorithm

The Luhn checksum is a simple algorithm that can be used to verify the validity of a credit card number. The algorithm works by adding the digits of the credit card number together, alternately doubling the digits in the odd-numbered positions and adding those digits without doubling. The final digit is then subtracted from 10. If the remainder is 0, the credit card number is valid.

The Luhn algorithm is used in a variety of systems:

- Credit card numbers
- IMEI numbers
- National Provider Identifier numbers in the United States
- Canadian social insurance numbers
- Israeli ID numbers
- South African ID numbers
- Swedish national identification numbers
- Swedish Corporate Identity Numbers (OrgNr)
- Greek Social Security Numbers (ΑΜΚΑ)
- SIM card numbers
- European patent application numbers
- Survey codes appearing on McDonald's, Taco Bell, and Tractor Supply Co. receipts

# Description - Check Digit Computation

Summing Odd Digits: Initialize a variable sum_odd_digits to 0. Starting from the rightmost digit (which is the 15th digit), iterate over every other digit (odd positions) and add them to sum_odd_digits.

Doubling and Summing Even Digits: Initialize a variable sum_even_digits to 0. Starting from the second-to-last digit (which is the 14th digit), iterate over every other digit (even positions). Double the digit's value, and if the result is greater than or equal to 10, split the result into its digits and add them together. Add the final result to sum_even_digits.

Total Sum: Add sum_odd_digits and sum_even_digits to get the total sum.

Check Digit Calculation: Check if the total sum is divisible by 10. If it is, the check digit is 0. If it's not, calculate the difference needed to make the total sum a multiple of 10. This is done by finding the smallest multiple of 10 greater than the total sum (using math.ceil(total / 10) * 10) and then subtracting the total sum from it. The result is the check digit.

## IMEI

The check digit is not transmitted over the radio interface, nor is it stored in the EIR database at any point. Therefore, all references to the last three or six digits of an IMEI refer to the actual IMEI number, to which the check digit does not belong.

## Credit Cards

The last digit is the Luhn check digit.