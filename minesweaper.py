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

    drawBoard(squaresData)



def drawBoard(sqaures):
    board = ""
    
    for row in sqaures:
        line = " "
        for sqaure in row:
            
                if sqaure["placed"] == True:
                    if sqaure["value"] == "mine":
                        line += f"[>]"
                    else:
                        line += f"[{sqaure["value"]}]"
                else:
                    line += f"[ ]"
        board += line+ "\n"
    print(board)

def predictSquareValue(sqaures, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if sqaures[i][j]["value"] != "mine":
                sqauresAround = []
                for x in range(i - 1, i + 2):
                    for y in range(j - 1 , j + 2):
                        if x >= 0 and x <= rows - 1 and  y >= 0 and y <= columns - 1:
                            if x == i and y == j:
                                pass
                            else:
                                sqauresAround.append(sqaures[x][y])
                    
                    

                mineCount = 0
                for sqaure in sqauresAround:
                    if sqaure["value"] == "mine":
                        mineCount += 1
                
                sqaures[i][j]["value"] = mineCount

    return sqaures

def startPlacement(num, rows, columns):
    randomPlace = 0


            

        
          


createBoard(20, 20)
