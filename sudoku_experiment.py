import random
import time
import json
from datetime import datetime

class Sudoku:
    
    space = {"value": "", "placed": False, "position": ""}
    tries = 3
    current_file = ""
    

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
                if self.board[i][j]["value"] != " " and self.board[i][j]["value"] != "":
                    count += 1
        if count == 81:
            return True
        else:
            return False

    def getLengths(self, _list):
        len_list = []
        for i in range(9):
                count = 0
                for j in range(9):
                    if _list[i][j]["value"] == " " or _list[i][j]["value"] == "":
                        count += 1
                len_list.append(count)
        return len_list

    def convertPos(self, x, y, _type):
        match _type:
            case "row":
                return x, y
            case "column":
                return y, x
            case "group":
                pos = self.groups[x][y]["position"]
                return int(pos[0]), int(pos[2])
            case _:
                return x, y

    
    #Solving Algorithms

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
    
    def solvePerFound(self, value, length_list, _list, _type):
        done = False
        if value in length_list:
            for j in range(length_list.count(value)):
                index_of_smallest = length_list.index(value)
                for k in range(9):
                    if _list[index_of_smallest][k]["value"] == " ":
                        x, y = self.convertPos(index_of_smallest, k, _type)
                        done = self.solveSquare(x, y)
                        break
                length_list[index_of_smallest] = 0
        
        return done

    def solveByRemainder(self):
        done = False
        for _ in range(self.tries):
            if done == True: break
            

            self.loadData()
            self.displayBoard()

            runtime  = 0

            done_r = True
            done_c = True
            done_g = True

            

            

            while done == False and runtime < 100:
                runtime += 1
                self.rows, self.columns, self.groups = self.divideBoard()
                
                len_rows = self.getLengths(self.rows)
                len_columns = self.getLengths(self.columns)
                len_groups = self.getLengths(self.groups)
                
                # print()
                # print(len_rows)
                # print(len_columns)
                # print(len_groups)
                # print()
                
                i = 1
                # for __ in range(4):
                count = 0
                len_rows = self.getLengths(self.rows)
                len_columns = self.getLengths(self.columns)
                len_groups = self.getLengths(self.groups)                 


                # if i in len_rows or i in len_columns or i in len_rows:
                #     done_r = self.solvePerFound(i, len_rows, self.rows, "row")
                #     done_c = self.solvePerFound(i, len_columns, self.columns, "column")
                #     done_g = self.solvePerFound(i, len_groups, self.groups, "group")

                #     print(done_r, done_c, done_g)

                #     if done_r == False and done_c == False and done_g == False:
                #         if i < 9 : i+= 1
                #         else: i = 1

                # else:
                #     print(i)
                #     if i < 9 : i+= 1
                #     else: i = 1

                
                
                

                if done_r == False and done_c == False and done_g == False:
                    if i < 9 : i += 1
                    else: i = 1
                    continue
                else:
                    for j in range(1,10):
                        if j in len_rows or j in len_columns or j in len_rows:
                            i = j
                            break

                done_r = self.solvePerFound(i, len_rows, self.rows, "row")
                done_c = self.solvePerFound(i, len_columns, self.columns, "column")
                done_g = self.solvePerFound(i, len_groups, self.groups, "group")

                print("\n", done_r, done_c, done_g, "\n")

                done = self.checkDone()

            print(f"Tries: [{_}]")

            

            

            


    def test(self, counts, solvingMethod):
        data = []
        for i in range(counts):
            
            self.createBoard()
            print(f"\nCount: {i+1}")
            solvingMethod()
            self.displayBoard()
            data.append(self.calculatePercentage())

        self.saveData(data)
            



#
game =  Sudoku()
game.current_file = "2"
game.tries = 10
# game.inputBoardData()
game.solveByRemainder()
game.displayBoard()
print(game.calculatePercentage())
    
