white_possibles = list(range(1,70)) # white balls range from 1 to 69
red_possibles = list(range(1,27)) # 26 possibiles for power ball

tickets_per_drawing = 5 # I bought 5 tickets for each drawing spending $10/draw 
num_drawings = 156 # 156 drawings per year

total_spent = 0
earnings = 0

#keep track of outcomes
times_won = {
    "5+P":0,
    "5":0,
    "4+P":0,
    "4":0,
    "3+P":0,
    "3":0,
    "2+P":0,
    "1+P":0,
    "P":0,
    "0":0,
}


# What did I win?
def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0

    # set intersection will give numbers that matched
    # len will give how many numbers matched
    white_matches = len(my_numbers['whites'].intersection(winning_numbers['whites']))

    power_match = my_numbers['red'] == winning_numbers['red']

    # How much did I win?
    if white_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won['5+P'] += 1
        else:
            win_amt = 1_000_000
            times_won['5'] += 1 
    elif white_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won['4+P'] += 1
        else:
            win_amt = 100
            times_won['4'] += 1
    elif white_matches == 3:
        if power_match:
            win_amt = 100
            times_won['3+P'] += 1
        else:
            win_amt = 7
            times_won['3'] += 1
    elif white_matches == 2 and power_match:
        win_amt = 7
        times_won['2+P'] += 1
    elif white_matches == 1 and power_match:
        win_amt = 4
        times_won['1+P'] += 1
    elif power_match:
        win_amt = 4
        times_won['P'] += 1
    else:
        times_won['0'] += 1
    return win_amt


import random
import json
for drawing in range(num_drawings):
    # random sample of 5 unique balls
    white_drawing = set(random.sample(white_possibles, k=5))
    # print(white_drawing)

    red_drawing = random.choice(red_possibles)
    # print(red_drawing)

    winning_numbers = {
        'whites': white_drawing, 'red': red_drawing
    }

    # Buy the tickets (randomly bought, not chosen)
    for ticket in range(tickets_per_drawing):
        total_spent += 2 # $2 per ticket
        my_whites = set(random.sample(white_possibles,k=5))
        my_red = random.choice(red_possibles)

        my_numbers = {'whites': my_whites, 'red': my_red}

        # Call Function
        win_amt = calc_win_amt(my_numbers, winning_numbers)

        # Earnings
        earnings += win_amt

print(f'Spent: ${total_spent}')
print(f'Earnings: ${earnings}')


print(json.dumps(times_won, indent=2))