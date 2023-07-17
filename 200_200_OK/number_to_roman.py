def number_to_roman(num):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    
    for value, symbol in roman_numerals.items():
        while num >= value:
            roman_numeral += symbol
            num -= value
    
    return roman_numeral

num = 200
roman = number_to_roman(num)
print(f"The Roman numeral representation of {num} is: {roman}")
