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

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

turnCounter = 0
while True:
    pass