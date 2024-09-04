import random
import time
import json
from datetime import datetime

class Sudoku:
    current_file = ""
    space = {"value": "", "placed": False, "position": ""}
    

    def __init__(self) -> None:
        self.board = []
        self.rows = []
        self.columns = []
        self.groups = []
        self.createBoard()
        # self.solveDiagonals()
        # self.displayBoard()
        # print("\n")

    def createBoard(self):
        self.board = []
        x = 1
        for i in range(9):
            row = []
            for j in range(9):
                    row.append({"value": "", "placed": False, "position": f"{i}-{j}", "group": "0"})
                    x += 1
            self.board.append(row)
        

    def displayBoard(self):
        for i in range(9):
            line = ""
            for j in range(9):
                if self.board[i][j]["value"] != "":
                    line += f"[{self.board[i][j]["value"]}]"
                else:
                    line += "[ ]"
            print(line)

    def divideBoard(self):
        #
        rows = self.board
        columns = []
        groups = []

        for i in range(9):
            column = []
            for j in range(9):
                column.append(self.board[j][i])
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
                        group.append(self.board[j][k])
                        self.board[j][k]["group"] = str(len(groups))

                if k_start == 6: k_start = 0
                else: k_start += 3
                groups.append(group)
            if j_start == 6: j_start = 0
            else: j_start += 3


        return rows, columns, groups

    def saveData(self, DATA):
        print("\nSaving Board Data....")
        cureentTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"./Sudoku/report-{cureentTime}.json", "w") as file:
            json.dump(DATA, file, indent=4)
        time.sleep(2)
        print(f"Saved Board Data To: {f"./Sudoku/{cureentTime}.json"}")

    def loadData(self):
        print("\nLoading Board Data....")
        with open(f"./Sudoku/test-board{self.current_file}.json", "r") as file:
            data = json.load(file)
            for i in range(9):
                for j in  range(9):
                    self.board[i][j]["value"] = data[str(i)][j]

        return self.board
            


    def inputBoardData(self):
        rows = {}
        for i in range(9):
            row = input(f"input row [{i + 1}]: ")
            rows[i] = row
        print("\nSaving Board Data....")
        with open(f"./Sudoku/test-board{self.current_file}.json", "w") as file:
            json.dump(rows, file, indent=4)


    def calculatePercentage(self):
        empty = 0
        empty_pos = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j]["value"] == "" or self.board[i][j]["value"] == " ":
                    empty += 1
                    empty_pos.append(self.board[i][j]["position"])
        print(f"Not Done: {empty}\n{empty_pos}")
        print(f"{int(((81-empty)/81) * 100)}% Complete")

        return {
            "no": empty,
            "complete": f"{int(((81-empty)/81) * 100)}%",
            "pos": empty_pos
        }

    #TODO: Solving algorithm
    def findWithPos(self, pos):
        row = int(pos[0])
        column = int(pos[2])
        group = int(self.board[row][column]["group"])

        return row, column, group

    def crossCheck(self, value, row, column, group):
        self.rows, self.columns, self.groups = self.divideBoard()
            
        for j in self.rows[row]:
            if value == j["value"]: return False

        for j in self.columns[column]:
            if value == j["value"]: return False

        for j in self.groups[group]:
            if value == j["value"]: return False
        
        return True

    def checkDone(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j]["value"] != " ":
                    count += 1
        if count == 81:
            return True
        else:
            return False

    #Solving Algorithms
    def solveDiagonals(self):

        pos_nums = list(range(1, 10))
        sets = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
        ]

        for i in range(3):
            self.solveGroup(sets[i], sets[i])

        sets = [
            [0,1,2],
            [6,7,8],
            [0,1,2],
        ]

        for i in range(2):
            self.solveGroup(sets[i], sets[i + 1])

    def solveGroup(self, set1, set2):
        pos_nums = list(range(1, 10))
        for j in set1:
                for k in set2:
                    if self.board[j][k]["value"] == "" or self.board[j][k]["value"] == " ":
                        
                        row, column, group = self.findWithPos(f"{j}-{k}")
                        while True:
                            try:
                                value = random.choice(pos_nums)
                                if self.crossCheck(str(value), row, column, group):
                                    self.board[j][k]["value"] = str(value)
                                    break
                                else:
                                    pos_nums.remove(value)
                            except IndexError:
                                break
                    else:
                        continue
    
    def solveSquare(self, x, y):
        pos_nums = list(range(1, 10))
        row, column, group = self.findWithPos(f"{x}-{y}")
        while True:
            try:
                value = random.choice(pos_nums)
                if self.crossCheck(str(value), row, column, group):
                    self.board[x][y]["value"] = str(value)
                    # print(f"Placed at {x}-{y}")
                    return True
                else:
                    pos_nums.remove(value)
                    # if x == 2 and y == 7: print(f"cant place {value}")
            except IndexError:
                break
        return False
    
    def solveByGroups(self):
        sets = [
            [[0,1,2], [0,1,2]],
            [[0,1,2], [3,4,5]],
            [[0,1,2], [6,7,8]],
            [[3,4,5], [0,1,2]],
            [[3,4,5], [3,4,5]],
            [[3,4,5], [6,7,8]],
            [[6,7,8], [0,1,2]],
            [[6,7,8], [3,4,5]],
            [[6,7,8], [6,7,8]]
        ]
        for i in range(9):
            self.solveGroup(sets[i][0], sets[i][1])
        print("")
        self.displayBoard()

    def solveByRow(self):        

        # print("\nSolving.....\n")
        # self.solveDiagonals()
        
        # board = self.loadData()
        # game.displayBoard()

        self.loadData()
        game.displayBoard()

        while self.checkDone() == False :
            self.loadData()
            print("solving.....")
            for i in range(9):
                for j in range(9):
                    if self.board[i][j]["value"] == "" or self.board[i][j]["value"] == " ":
                        pos_nums = list(range(1, 10))
                        row, column, group = self.findWithPos(f"{i}-{j}")
                        while True:
                            try:
                                value = random.choice(pos_nums)
                                if self.crossCheck(str(value), row, column, group):
                                    self.board[i][j]["value"] = str(value)
                                    break
                                else:
                                    pos_nums.remove(value)
                            except IndexError:
                                break
                    else:
                        continue
        
        print("")
        self.displayBoard()



#
game =  Sudoku()
game.current_file = "-easy"
# game.inputBoardData()
game.solveWithStepBack()
game.displayBoard()
print(game.calculatePercentage())
    
