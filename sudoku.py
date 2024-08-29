import random
space = {"value": "", "placed": False, "position": ""}


def createBoard():
    board = []

    pos_nums = list(range(1, 10))

    x = 1
    for i in range(9):
        row = []
        for j in range(9):
                row.append({"value": "", "placed": False, "position": f"{i}-{j}"})
                x += 1
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

    # squares = []

    # for i in board:
    #     for j in i:
    #         squares.append(j)


    #
    for i in range(9):
        column = []
        for j in range(9):
            column.append(board[j][i])
        columns.append(column)

    #
    j_start = 0
    k_start = 0
    
    for x in range(3):
        for i in range(3):
            j_stop = j_start + 3
            group = []
            for j in range(j_start, j_stop):
                k_stop = k_start + 3
                
                for k in range(k_start, k_stop):
                    group.append(board[j][k])
                    board[j][k]["group"] = str(len(groups))

            if k_start == 6: k_start = 0
            else: k_start += 3
            groups.append(group)
        if j_start == 6: j_start = 0
        else: j_start += 3

        
        
                



    return rows, columns, groups

def test():
    board = createBoard()
    rows, columns, groups = divideBoard(board)

    print("Columns")
    for i in range(9):
        
        line = f"{i}:"
        for j in range(9):
            line += columns[i][j]["value"]
        print(line)

    print("Rows")
    for i in range(9):
        
        line = f"{i}:"
        for j in range(9):
            line += rows[i][j]["value"]
        print(line)

    print("Groups")
    if len(groups) > 0:
        for i in range(9):
            
            line = f"{i}:"
            for j in range(9):
                line += groups[i][j]["value"]
            print(line)

    row, column, group = findWithPos("1-2", board)
    print(crossCheck(input(": "), rows, columns, groups, row, column, 2))

    


#TODO: Solving algorithm
def findWithPos(pos, board):
    row = int(pos[0])
    column = int(pos[2])
    group = int(board[row][column]["group"])

    print(board[row][column]["value"])

    return row, column, group

def crossCheck(value, rows, columns, groups, row, column, group):
        for j in rows[row]:
            if value == j["value"]: return False

        for j in columns[column]:
            if value == j["value"]: return False

        for j in groups[group]:
            if value == j["value"]: return False
        
        return True


def Solve():
    pass



test()

