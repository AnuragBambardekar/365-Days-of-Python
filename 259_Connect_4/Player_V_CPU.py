import random

text = "Connect Four Game"
line = '-' * ((60 - len(text)) // 2) # 60 is the line length
print(f'{line}{text}{line}') 
# dotted_line = '-' * 20
# print(f'{dotted_line}')

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","","",],["","","","","","","",],
             ["","","","","","","",],["","","","","","","",],
              ["","","","","","","",],["","","","","","","",], ]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")

        for y in range(cols):
            if(gameBoard[x][y] == "🔵"): # WINKEY + . to access emojis
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🔴"):
                print("",gameBoard[x][y], end=" |")
            else:
                print(" ",gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

# printGameBoard()

# def modifyArray(spacePicked, turn):
#     gameBoard[spacePicked[0]][spacePicked[1]] = turn

# def checkForWinner(chip):
#     # check for horizontal spaces
#     for y in range(rows):
#         for x in range(cols - 3):
#             if (gameBoard[x][y]==chip and gameBoard[x+1][y]==chip and gameBoard[x+2][y]==chip and gameBoard[x+3][y]==chip):
#                 print("\nGame Over!",chip, " wins! Thank you for playing. :)")
#                 return True
            
#     # check for vertical spaces
#     for y in range(rows):
#         for x in range(cols - 3):
#             if (gameBoard[x][y]==chip and gameBoard[x][y+1]==chip and gameBoard[x][y+2]==chip and gameBoard[x][y+3]==chip):
#                 print("\nGame Over!",chip, " wins! Thank you for playing. :)")
#                 return True
            
#     # check for diagonal spaces (Top Right to Bottom Left)
#     for y in range(rows - 3):
#         for x in range(3, cols):
#             if (gameBoard[x][y]==chip and gameBoard[x+1][y-1]==chip and gameBoard[x+2][y-2]==chip and gameBoard[x+3][y-3]==chip):
#                 print("\nGame Over!",chip, " wins! Thank you for playing. :)")
#                 return True
            
#     # check for diagonal spaces (Top Left to Bottom Right)
#     for y in range(rows - 3):
#         for x in range(cols - 3):
#             if (gameBoard[x][y]==chip and gameBoard[x+1][y+1]==chip and gameBoard[x+2][y+2]==chip and gameBoard[x+3][y+3]==chip):
#                 print("\nGame Over!",chip, " wins! Thank you for playing. :)")
#                 return True

#     return False

# def coordinateParser(inputString):
#     coordinate = [None] * 2
#     if(inputString[0] == "A"):
#         coordinate[1] = 0
#     elif(inputString[0] == "B"):
#         coordinate[1] = 1
#     elif(inputString[0] == "C"):
#         coordinate[1] = 2
#     elif(inputString[0] == "D"):
#         coordinate[1] = 3
#     elif(inputString[0] == "E"):
#         coordinate[1] = 4
#     elif(inputString[0] == "F"):
#         coordinate[1] = 5
#     elif(inputString[0] == "G"):
#         coordinate[1] = 6
#     else:
#         print("Invalid")
#     coordinate[0] = int(inputString[1])
#     return coordinate

# def isSpaceAvailable(intendedCoordinate):
#     if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]]=="🔴"):
#         return False
#     elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]]=="🔵"):
#         return False
#     else:
#         return True

# def gravityChecker(intendedCoordinate):
#     # calculate space below
#     spaceBelow = [None] * 2
#     spaceBelow[0] = intendedCoordinate[0] + 1
#     spaceBelow[1] = intendedCoordinate[1]

#     # is coordinate at ground level
#     if(spaceBelow[0] == 6):
#         return True
    
#     # check if there is a token below
#     if(isSpaceAvailable(spaceBelow) == False):
#         return True
    
#     return False


# turnCounter = 0
# while True:
#     if(turnCounter % 2 == 0):
#         printGameBoard()
#         while True:
#             spacePicked = input("\nChoose a space: ")
#             coordinate = coordinateParser(spacePicked)
#             try:
#                 # check if space is available
#                 if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
#                     modifyArray(coordinate, '🔵')
#                     break
#                 else:
#                     print("Not a valid coordinate")
#             except:
#                 print("Error occured, please try Again!")
#         winner = checkForWinner("🔵")
#         turnCounter += 1
#     else:
#         while True:
#             cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
#             cpuCoordinate = coordinateParser(cpuChoice)
#             if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
#                 modifyArray(cpuCoordinate, "🔴")
#                 break
#         turnCounter += 1
#         winner = checkForWinner("🔴")

#     if(winner):
#         printGameBoard()
#         break


def is_valid_move(column):
    return 0 <= column < cols and gameBoard[0][column] == ""


def drop_piece(column, player):
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][column] == "":
            gameBoard[row][column] = player
            return True
    return False


def check_winner(player):
    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == player and gameBoard[row][col + 1] == player and \
                    gameBoard[row][col + 2] == player and gameBoard[row][col + 3] == player:
                return True

    # Check vertical
    for row in range(rows - 3):
        for col in range(cols):
            if gameBoard[row][col] == player and gameBoard[row + 1][col] == player and \
                    gameBoard[row + 2][col] == player and gameBoard[row + 3][col] == player:
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == player and gameBoard[row - 1][col + 1] == player and \
                    gameBoard[row - 2][col + 2] == player and gameBoard[row - 3][col + 3] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3, rows):
        for col in range(3, cols):
            if gameBoard[row][col] == player and gameBoard[row - 1][col - 1] == player and \
                    gameBoard[row - 2][col - 2] == player and gameBoard[row - 3][col - 3] == player:
                return True

    return False


def is_board_full():
    for col in range(cols):
        if gameBoard[0][col] == "":
            return False
    return True


def cpu_move():
    while True:
        column = random.randint(0, cols - 1)
        if is_valid_move(column):
            return column


def play_connect_four():
    player_turn = "🔵"
    game_over = False

    while not game_over:
        printGameBoard()

        if player_turn == "🔵":
            print("\nPlayer", player_turn, "turn")
            column = input("Select a column (A-G): ").upper()

            if column in possibleLetters:
                column = possibleLetters.index(column)
                if is_valid_move(column):
                    if drop_piece(column, player_turn):
                        if check_winner(player_turn):
                            printGameBoard()
                            print("Player", player_turn, "wins! Congratulations!")
                            game_over = True
                        elif is_board_full():
                            printGameBoard()
                            print("It's a draw! The board is full.")
                            game_over = True
                        else:
                            player_turn = "🔴"
                    else:
                        print("Column is full. Try again.")
                else:
                    print("Invalid column. Try again.")
            else:
                print("Invalid input. Enter a valid column (A-G).")
        else:
            print("\nCPU's turn")
            column = cpu_move()
            if is_valid_move(column):
                print("CPU selects column", possibleLetters[column])
                if drop_piece(column, player_turn):
                    if check_winner(player_turn):
                        printGameBoard()
                        print("Player", player_turn, "wins! Congratulations!")
                        game_over = True
                    elif is_board_full():
                        printGameBoard()
                        print("It's a draw! The board is full.")
                        game_over = True
                    else:
                        player_turn = "🔵"
                else:
                    print("Column is full. Try again.")


if __name__ == "__main__":
    play_connect_four()