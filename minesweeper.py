import random

def createBoard(rows, columns):
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

    return squaresData



def drawBoard(squares, rows, columns):
    board = "      "
    for i in range(columns):
        board += f"[{i}]"
    board += "\n"
    
    j = 0
    for r in squares:
        line = f" [{j}] "
        if j < 10:
            line += " "
        j += 1 
        for square in r:
            
                if square["placed"] == True:
                    if square["value"] == "mine":
                        line += f"[>]"
                    else:
                        line += f"[{square["value"]}]"
                else:
                    line += f"[ ]"
        board += line+ "\n"
    print(board)

def predictSquareValue(squares, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if squares[i][j]["value"] != "mine":
                squaresAround = []
                for x in range(i - 1, i + 2):
                    for y in range(j - 1 , j + 2):
                        # if x >= 0 and x <= rows - 1 and  y >= 0 and y <= columns - 1:
                        #     if x == i and y == j:
                        #         pass
                        #     else:
                        #         squaresAround.append(squares[x][y])

                        if x == i  and y == j:
                            pass
                        else:
                            try:
                                squaresAround.append(squares[x][y])
                            except IndexError:
                                continue
                    
                    

                mineCount = 0
                for square in squaresAround:
                    if square["value"] == "mine":
                        mineCount += 1
                
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

def start(rows = 20, columns = 10):
    squares = createBoard(rows, columns)
    print("""
How to play:
Tpye the row-column number, eg 1-0
Then type the what you want to place there, wether a flag [>] or an empty [_]
If your playing this you should already know how to play minesweeper,
If you don't then go and learn
""")
    while True:
        drawBoard(squares, rows, columns)

        pos_response = input("input row-column: ")
        val_response = input("input what you want to place there: ")

        if len(pos_response) == 3 and val_response == "flag" or ">" or "empty" or "_":
            if place(pos_response, val_response, squares) :
                continue
            else:
                print("You placed on a mine. Game Over")
                break
        else:
            print("your input is not correct, type the right syntax")
            continue
        
    response = input("Dou you want to play again: ")
    if response.lower() == "yes":
        start()
    else:
        return 0
    

start()


            

        
          



