import random
space = {"value": "", "placed": False, "position": ""}


def createBoard():
    board = []

    pos_nums = list(range(1, 10))

    for i in range(9):
        row = []
        for j in range(9):
                row.append({"value": "", "placed": False, "position": f"{i}-{j}"})
        board.append(row)

    sets = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]

    for i in range(3):
        num = 0
        random.shuffle(pos_nums)
        for j in sets[i]:
            for k in sets[i]:
                board[j][k]["value"] = str(pos_nums[num])
                num += 1

    displayBoard(board)

    return board

def displayBoard(board):
    for i in range(9):
        line = ""
        for j in range(9):
            if board[i][j]["value"] != "":
                line += f"[{board[i][j]["value"]}]"
            else:
                line += "[ ]"
        print(line)

def divideBoard(board):
    #
    rows = board
    columns = []
    groups = []


    #
    for i in range(9):
        column = []
        for j in range(9):
            column.append(board[j][i])
        columns.append(column)


    return rows, columns, groups


rows, columns, groups = divideBoard(createBoard())

for i in range(9):
    print("Columns")
    line = f"{i}:"
    for j in range(9):
        line += columns[i][j]["value"]
    print(line)


#TODO: Solving algorithm



