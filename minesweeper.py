import random
from datetime import datetime
import time
import json

def createBoard(rows = 20, columns = 10):
    numSquares = rows * columns
    numMines = numSquares / 4
    squaresData = []
    squares = []

    for i in range(rows):
        row = []
        for j in range(columns):
            square = f"{i}-{j}"
            row.append({
                "value": " ",
                "square": square,
                "placed": False
            })
            squares.append(square)
        squaresData.append(row)

    mines = []
    for mine in range(int(numMines)):
        i = random.randint(0, rows - 1)
        j = random.randint(0, columns - 1 )
        squaresData[i][j]["value"] = "mine"

        mines.append(squaresData[i][j])

    predictSquareValue(squaresData, rows, columns)

    #Make sure that there are no zero
    for i in range(rows):
        for j in range(columns):
            if squaresData[i][j]["value"] == 0:
                squaresData[i][j]["value"] = "mine"

    predictSquareValue(squaresData, rows, columns)
    startPlacement(rows, columns, squaresData, 5)

    return squaresData, numMines

def drawBoard(squares, rows = 20, columns = 10, test = False):
    board = "      "
    for i in range(columns):
        board += f"[{i}]"
    board += "\n\n"
    
    j = 0
    for r in squares:
        line = f" [{j}] "
        if j < 10:
            line += " "
        j += 1 
        for square in r:
            
                if test == False:
                    if square["placed"] == True:
                        if square["value"] == "mine":
                            line += f"[>]"
                        else:
                            line += f"[{square["value"]}]"
                    else:
                        line += f"[ ]"
                else:
                    if square["value"] == "mine":
                        line += f"[>]"
                    else:
                        line += f"[{square["value"]}]"
        board += line+ "\n"
    print(board)

def predictSquareValue(squares, rows, columns):
    for i in range(rows):
        for j in range(columns):
            
                squaresAround = []
                for x in range(i - 1, i + 2):
                    for y in range(j - 1 , j + 2):
                        if x >= 0 and x <= rows - 1 and  y >= 0 and y <= columns - 1:
                            if x == i and y == j:
                                pass
                            else:
                                squaresAround.append(squares[x][y])

                        # if x == i  and y == j:
                        #     pass
                        # else:
                        #     try:
                        #         squaresAround.append(squares[x][y])
                        #     except IndexError:
                        #         continue
                    
                    

                mineCount = 0
                for square in squaresAround:
                    if square["value"] == "mine":
                        mineCount += 1
                

                if squares[i][j]["value"] != "mine":
                    squares[i][j]["value"] = mineCount
                else:
                    if mineCount == len(squaresAround):
                       squares[i][j]["value"] = mineCount 

    return squares

def startPlacement(rows, columns, squares, margin = 2):
    i = random.randint(0 + margin, rows - margin)
    j = random.randint(0 - margin, columns - margin )

    num = random.randint(4, 6)

    for x in range(i - int(num/2), i + int(num/2) ):
        for y in range(j - int(num/2), j + int(num/2) ):
            if squares[x][y]["value"] != "mine":
                squares[x][y]["placed"] = True

def place(position, value, squares):
    i = 0
    j = 0

    if len(position) > 3:
        i = int(position[0] + position[1])
        j = int(position[3])
    else:
        i = int(position[0])
        j = int(position[2])

    try:
        if value == "flag" or value == ">" and squares[i][j]["value"] == "mine":
            squares[i][j]["placed"] = True
        elif value == "empty" or value == "_" and squares[i][j]["value"] != "mine":
            squares[i][j]["placed"] = True
        else:
            return False
    except ValueError:
        return False
    
    return True

def saveData(board):
    print("\nSaving Board Data....")
    cureentTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    location = f"./Minesweeper/{cureentTime}.json"
    with open(location, "w") as file:
        json.dump(board, file, indent=4)
    time.sleep(2)
    print(f"Saved Board Data To: {location}")

def test():
    squares = createBoard()
    drawBoard(squares, test=True)
    pass

def start_ver_1(rows = 20, columns = 10):
    squares, numMines = createBoard(rows, columns)
    numMines = int(numMines)
    print("""
How to play:
Tpye the row-column number, eg 1-0
Then type the what you want to place there, wether a flag [>] or an empty [_]
Be very carefull where you place your empties, bcos they can make you lose the game and there are no do overs.
If your playing this you should already know how to play minesweeper,
If you don't then go and learn
""")
    while True:
        print(f"Number of Mines [>] left : {numMines}\n")
        drawBoard(squares, rows, columns)

        pos_response = input("input row-column: ")
        val_response = input("input what you want to place there: ")

        if len(pos_response) == 3 and val_response == "flag" or ">" or "empty" or "_":
            if val_response == "flag" or ">": numMines -= 1
            if place(pos_response, val_response, squares) :
                continue
            else:
                print("You placed on a mine. Game Over")
                print("""
                ___ ___
                (.) (.)
                   ^
               [-------]
""" + ("SMH "*10))
                break
        else:
            print("your input is not correct, type the right syntax")
            continue
        
    response = input("Dou you want to play again: ")
    if response.lower() == "yes":
        start_ver_1(rows=rows, columns= columns)
    else:
        return 0
    
def start_ver_2(rows = 20, columns = 10):
    squares, numMines = createBoard(rows, columns)
    numMines = int(numMines)
    val_response = ">"
    pos_response = ""
    print("""
How to play:
Tpye the row-column number, eg 1-0
Then type what you want to place there, wether a flag [>] or an empty [_]
Be very carefull where you place your empties, bcos they can make you lose the game and there are no do overs.
If your playing this you should already know how to play minesweeper,
If you don't then go and learn
""")
    while True:
        print(f"Number of Mines [>] left : {numMines}\nYou are cureently using a {val_response}")
        drawBoard(squares, rows, columns)

        response = input("Input either a position or a flag [>] or empty [_] : ")

        if response == "flag" or response == ">" or response == "empty" or response == "_": 
            val_response = response
            continue
        else:
            pos_response = response


        if len(pos_response) == 3 and val_response == "flag" or ">" or "empty" or "_":


            if val_response == "flag" or ">" and numMines > 0: 
                numMines -= 1
            else: 
                print("Your out of flags")
                break


            if place(pos_response, val_response, squares) :
                continue
            else:
                print("You stepped on a mine. Game Over")
                print("""
                ___ ___
                (.) (.)
                   ^
               [-------]
""" + ("SMH "*10))
                break
        else:
            print("your input is not correct, type the right syntax")
            continue
        
    response = input("Dou you want to play again: ")
    saveData({"squares": squares, "rows": rows, "columns": columns})
    if response.lower() == "yes":
        start_ver_2(rows=rows, columns=columns)
    else:
        return 0
    




#start_ver_1()
start_ver_2()

# test()

            

        
          



