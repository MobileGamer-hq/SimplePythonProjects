class Chess():

    space = {"value": "", "empty": False, "position": "", "color": ""}
    pieces = {
        "castle": "C",
        "knight": "K",
        "bishop": "B",
        "queen": "Q",
        "king": "K",
        "pawn": "P"
    }

    def __init__(self) -> None:
        self.board = self.createBoard()
        self.drawBoard()
        pass

    #
    def createBoard(self):
        board = []

        for i in range(8):
            row = []
            for j in range(8):
                row.append({"value": " ", "position": f"{i}-{j}", "color": ""})
            board.append(row)

        for i in range(2):
            color = ""
            if i == 0: color = "white"
            else: color = "black"

            for j in range(8):
                if j == 0 or j == 7:
                    board[int(i * 7)][j]["value"] = self.pieces["castle"]
                elif j == 1 or j == 6:
                    board[int(i * 7)][j]["value"] = self.pieces["knight"]
                elif j == 2 or j == 5:
                    board[int(i * 7)][j]["value"] = self.pieces["bishop"]
                elif j == 3:
                    board[int(i * 7)][j]["value"] = self.pieces["queen"]
                elif j == 4:
                    board[int(i * 7)][j]["value"] = self.pieces["king"]

                

                board[int((i * 5) + 1)][j]["value"] = self.pieces["pawn"]

                # board[int(i * 7)][j]["empty"] = False
                # board[int((i * 5) + 1)][j]["empty"] = False

                board[int(i * 7)][j]["color"] = color
                board[int((i * 5) + 1)][j]["color"] = color


        board[3][4]["value"] = self.pieces["knight"]
        board[3][4]["color"] = "white"
            
        return board

    def drawBoard(self):
        for i in range(8):
            line = ""
            for j in range(8):
                line += f"[{self.board[i][j]["value"]}]"
            print(line)
            

    #
    def place(self, pos, kill = False):
        x = int(pos[0])
        y = int(pos[2])

        if kill: self.board[x][y]["value"] = "-"
        else: self.board[x][y]["value"] = "+"
    def playMove(self):
        pass

    # Prediction
    def checkEmpty(self, x, y):
        if self.board[x][y]["value"] == " ":
            return True
        else:
            return False
        
    def checkColor(self, x, y, color):
        if self.checkEmpty(x, y) == False:
            if self.board[x][y]["color"] == color:
                return True
            else:
                return False
        else:
            return False

    def possibleMoves(self, pos):
        startPos_x = int(pos[0])
        startPos_y = int(pos[2])

        piece = self.board[startPos_x][startPos_y]
        color = piece["color"]
        if piece["value"] == self.pieces["castle"]:
            return self.castleMoves(startPos_x, startPos_y, color)
        elif piece["value"] == self.pieces["knight"]:
            return self.knightMoves(startPos_x, startPos_y, color)
        elif piece["value"] == self.pieces["bishop"]:
            pass
        elif piece["value"] == self.pieces["queen"]:
            pass
        elif piece["value"] == self.pieces["king"]:
            pass
        elif piece["value"] == self.pieces["pawn"]:
            pass

    def castleMoves(self, x, y, color):

        possibleMoves = []

        for i in range(x + 1, 8):
            
            if self.checkColor(i, y, color) == False : 
                if self.checkEmpty(i, y):
                    possibleMoves.append({
                        "pos": self.board[i][y]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[i][y]["position"],
                        "kill" : True
                    })
                    break
            else:
                print(f"Broke for {i}-{y}")
                break
        for i in range(0, x):
            i = x - 1 - i
            if self.checkColor(i, y, color) == False : 
                if self.checkEmpty(i, y):
                    possibleMoves.append({
                        "pos": self.board[i][y]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[i][y]["position"],
                        "kill" : True
                    })
                    break
            else:
                print(f"Broke for {i}-{y}")
                break

        for i in range(y + 1, 8):
            if self.checkColor(x, i, color) == False : 
                if self.checkEmpty(x, i):
                    possibleMoves.append({
                        "pos": self.board[x][i]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x][i]["position"],
                        "kill" : True
                    })
                    break
            else:
                print(f"Broke for {x}-{i}")
                break
        for i in range(0, y):
            i = y - 1 - i
            if self.checkColor(x, i, color) == False : 
                if self.checkEmpty(x, i):
                    possibleMoves.append({
                        "pos": self.board[x][i]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x][i]["position"],
                        "kill" : True
                    })
                    break
            else:
                print(f"Broke for {x}-{i}")
                break

        return possibleMoves

    def knightMoves(self, x, y, color):
        possibleMoves = []

        def placePositiveVertical(x, y):
            if x + 2 < 8 and y - 1 > 0 and self.checkColor(x + 2, y - 1, color) == False : 
                if self.checkEmpty(x + 2, y - 1):
                    possibleMoves.append({
                        "pos": self.board[x+2][y - 1]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x + 2][y - 1]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {x + 2}-{y - 1}")

            if x + 2 < 8 and y + 1 > 0 and self.checkColor(x + 2, y + 1, color) == False : 
                if self.checkEmpty(x + 2, y + 1):
                    possibleMoves.append({
                        "pos": self.board[x+2][y + 1]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x + 2][y + 1]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {x + 2}-{y + 1}") 

        def placeNegativeVertical(x, y):
            if x - 2 < 8 and y - 1 > 0 and self.checkColor(x - 2, y - 1, color) == False : 
                if self.checkEmpty(x - 2, y - 1):
                    possibleMoves.append({
                        "pos": self.board[x - 2][y - 1]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x - 2][y - 1]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {x - 2}-{y - 1}")

            if x - 2 < 8 and y + 1 > 0 and self.checkColor(x - 2, y + 1, color) == False : 
                if self.checkEmpty(x - 2, y + 1):
                    possibleMoves.append({
                        "pos": self.board[x - 2][y + 1]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[x - 2][y + 1]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {x - 2}-{y + 1}") 
        
        def placePositiveHorizontal(x, y):
            if x + 2 < 8 and y - 1 > 0 and self.checkColor(x + 2, y - 1, color) == False : 
                if self.checkEmpty(y - 1, x + 2):
                    possibleMoves.append({
                        "pos": self.board[y - 1][x + 2]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[y - 1][x + 2]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {y - 1}-{x + 2}")

            if x + 2 < 8 and y + 1 > 0 and self.checkColor(x + 2, y + 1, color) == False : 
                if self.checkEmpty( y + 1, x + 2):
                    possibleMoves.append({
                        "pos": self.board[y + 1][x + 2]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[y + 1][x + 2]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {x + 2}-{y + 1}") 

        def placeNegativeHorizontal(x, y):
            if x - 2 < 8 and y - 1 > 0 and self.checkColor(x - 2, y - 1, color) == False : 
                if self.checkEmpty( y - 1, x - 2):
                    possibleMoves.append({
                        "pos": self.board[y - 1][x - 2]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[y - 1][x - 2]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {y - 1}-{x -2}")

            if x - 2 < 8 and y + 1 > 0 and self.checkColor(x - 2, y + 1, color) == False : 
                if self.checkEmpty(y + 1, x - 2,):
                    possibleMoves.append({
                        "pos": self.board[y + 1][x - 2]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[y + 1][x - 2]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {y + 1}-{x - 2}") 
        

        placePositiveVertical(x,y)
        placeNegativeVertical(x,y)
        placePositiveHorizontal(y,x)
        placeNegativeHorizontal(y,x)

        return possibleMoves
        

        

    def bishopMoves(self, x, y, color):
        pass 



    def start():
        pass


game = Chess()

moves = game.possibleMoves("3-4")

for i in moves:
    game.place(i["pos"], i["kill"])

game.drawBoard()
