def move_cursor(x, y):
    print(f'\033[{y};{x}H', end='')

# Move the cursor to row 5, column 10
move_cursor(70, 5)

# Continue printing text from this position
print("Cursor moved to (70, 5)")
