class Chess():

    space = {"value": "", "empty": False, "position": "", "color": ""}
    pieces = {
        "castle-white": "♖",
        "knight-white": "♘",
        "bishop-white": "♗",
        "queen-white": "♕",
        "king-white": "♔",
        "pawn-white": "♙",
        "castle-black": "♜",
        "knight-black": "♞",
        "bishop-black": "♝",
        "queen-black": "♛",
        "king-black": "♚",
        "pawn-black": "♟"
    }

    pieces = {
        "white-castle": "♖",
        "white-knight": "♘",
        "white-bishop": "♗",
        "white-queen": "♕",
        "white-king": "♔",
        "white-pawn": "♙",
        "black-castle": "♜",
        "black-knight": "♞",
        "black-bishop": "♝",
        "black-queen": "♛",
        "black-king": "♚",
        "black-pawn": "♟"
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
                row.append({"value": " ", "position": f"{i}-{j}", "color": "", "previous": ""})
            board.append(row)

        for i in range(2):
            color = ""
            if i == 0: color = "white"
            else: color = "black"

            for j in range(8):
                if j == 0 or j == 7:
                    board[int(i * 7)][j]["value"] = self.pieces[f"castle-{color}"]
                elif j == 1 or j == 6:
                    board[int(i * 7)][j]["value"] = self.pieces[f"knight-{color}"]
                elif j == 2 or j == 5:
                    board[int(i * 7)][j]["value"] = self.pieces[f"bishop-{color}"]
                elif j == 3:
                    board[int(i * 7)][j]["value"] = self.pieces[f"queen-{color}"]
                elif j == 4:
                    board[int(i * 7)][j]["value"] = self.pieces[f"king-{color}"]

                

                board[int((i * 5) + 1)][j]["value"] = self.pieces[f"pawn-{color}"]

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
    def placePossiblities(self, pos, kill = False):
        x = int(pos[0])
        y = int(pos[2])
        value = self.board[x][y]["value"]
        if kill: self.board[x][y]["value"] = "-"
        else: self.board[x][y]["value"] = "+"
        self.board[x][y]["previous"] = value

    def undoPlacement(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j]["value"] == "-" or self.board[i][j]["value"] == "+":
                    self.board[i][j]["value"] = self.board[i][j]["previous"]
        pass

    def move(self, start_pos, final_pos):
        start_x = int(start_pos[0])
        start_y = int(start_pos[2])

        final_x = int(final_pos[0])
        final_y = int(final_pos[2])

        #
        value = self.board[start_x][start_y]["value"] 
        color = self.board[start_x][start_y]["color"]
        previous = self.board[final_x][final_y]["previous"]

        #
        self.board[final_x][final_y]["value"] = value
        self.board[final_x][final_y]["color"] = color
        self.board[final_x][final_y]["previous"] = previous

        #
        self.board[start_x][start_y]["value"] = " "
        self.board[start_x][start_y]["color"] = ""
        self.board[start_x][start_y]["previous"] = value

    def playMove(self):
        pass

    # Prediction
    def checkEmpty(self, x, y):
        if self.board[x][y]["value"] == " ":
            return True
        else:
            return False
        
    def checkColor(self, x, y, color):
        print(x,y)
        if self.board[x][y]["value"] != " ":
            if self.board[x][y]["color"] == color: 
                return True
            else:
                return False
        else:
            
            return False
        
    def countPieces(self):
        black_pieces = {
            "♜": "",
            "♞": "",
            "♝": "",
            "♛": "",
            "♚": "",
            "♟": ""
        }
        white_pieces = {
            "♖": "",
            "♘": "",
            "♗": "",
            "♕": "",
            "♔": "",
            "♙": ""
        }

        for i in range(8):
            for j in range(8):
                if self.checkEmpty(i, j) == False:
                    if self.board[i][j]["color"] == "white":
                        white_pieces[self.board[i][j]["value"]] = self.board[i][j]["position"]
                    else:
                        black_pieces[self.board[i][j]["value"]] = self.board[i][j]["position"]

        print(black_pieces)
        print(white_pieces)



    def showPossibleMoves(self, pos):
        moves = self.possibleMoves(pos)
        print(*moves)

        for i in moves:
            self.placePossiblities(i["pos"], i["kill"])

        self.drawBoard()
        self.undoPlacement()

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
            if x + 2 < 8 and y - 1 >= 0 and self.checkColor(x + 2, y - 1, color) == False : 
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

            if x + 2 < 8 and y + 1 < 8 and self.checkColor(x + 2, y + 1, color) == False : 
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
            if x - 2 >= 0 and y - 1 >= 0 and self.checkColor(x - 2, y - 1, color) == False : 
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

            if x - 2 >= 0 and y + 1 >= 0 and self.checkColor(x - 2, y + 1, color) == False : 
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
            m = x - 1
            n = y + 2
            if  m >= 0 and n < 8 and self.checkColor(m, n, color) == False : 
                if self.checkEmpty(m, n):
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {m}-{n}")

            m = x + 1
            if m < 8 and n < 8 and self.checkColor(m, n, color) == False : 
                if self.checkEmpty( m, n):
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {m}-{n}") 

        def placeNegativeHorizontal(x, y):
            m = x - 1
            n = y - 2
            if m >= 0 and n >= 0 and self.checkColor(m, n, color) == False : 
                if self.checkEmpty(m, n):
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {m}-{n}")
            
            m = x + 1
            if m < 8 and n >= 0 and self.checkColor(m, n, color) == False : 
                if self.checkEmpty( m, n):
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : False
                    })
                else:
                    possibleMoves.append({
                        "pos": self.board[m][n]["position"],
                        "kill" : True
                    })
            else:
                print(f"Broke for {m}-{n}") 
        

        placePositiveVertical(x,y)
        placeNegativeVertical(x,y)
        placePositiveHorizontal(x, y)
        placeNegativeHorizontal(x, y)

        return possibleMoves
        
    def bishopMoves(self, x, y, color):
        possibleMoves = []
        
        for i in range(8): 
            m, n = i + 1 + x , i + 1 + y

            if m < 8 and n < 8 and m >= 0 and n >= 0:
                if self.checkColor(m, n, color) == False : 
                    if self.checkEmpty(m, n,):
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : False
                        })
                    else:
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : True
                        })
                        break
                else:
                    print(f"Broke for {m}-{n}")
                    break
            else:
                print(f"Broke for {m}-{n}")
                break
        
        for i in range(8): 
            m, n = x - (i + 1) , y + (i + 1)

            if m < 8 and n < 8 and m >= 0 and n >= 0:
                if self.checkColor(m, n, color) == False : 
                    if self.checkEmpty(m, n,):
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : False
                        })
                    else:
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : True
                        })
                        break
                else:
                    print(f"Broke for {m}-{n}")
                    break
            else:
                print(f"Broke for {m}-{n}")
                break
        
        for i in range(8): 
            m, n = x + (i + 1) , y - (i + 1)

            if m < 8 and n < 8 and m >= 0 and n >= 0:
                if self.checkColor(m, n, color) == False : 
                    if self.checkEmpty(m, n,):
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : False
                        })
                    else:
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : True
                        })
                        break
                else:
                    print(f"Broke for {m}-{n}")
                    break
            else:
                print(f"Broke for {m}-{n}")
                break
        
        for i in range(8): 
            m, n = x - (i + 1) , y - (i + 1)

            if m < 8 and n < 8 and m >= 0 and n >= 0:
                if self.checkColor(m, n, color) == False : 
                    if self.checkEmpty(m, n,):
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : False
                        })
                    else:
                        possibleMoves.append({
                            "pos": self.board[m][n]["position"],
                            "kill" : True
                        })
                        break
                else:
                    print(f"Broke for {m}-{n}")
                    break
            else:
                print(f"Broke for {m}-{n}")
                break
        

        return possibleMoves

    def kingMoves(self, x, y, color):
        possibleMoves = []

        for i in range(x - 1, x + 2):
            for j in range(y - 1 , y + 2):
                if i >= 0 and i < 8 and  j >= 0 and j < 8:
                    if i == x and j == y:
                        pass
                    else:
                        if self.checkColor(i, j, color) == False :
                            if self.checkEmpty(i, j):
                                possibleMoves.append({
                                    "pos": self.board[i][j]["position"],
                                    "kill" : False
                                })
                            else:
                                possibleMoves.append({
                                    "pos": self.board[i][j]["position"],
                                    "kill" : True
                                })
                        else:
                            pass

        return possibleMoves




    def test(self, x, y, value, color = "white"):
        self.board[x][y]["value"] = self.pieces[value]
        self.board[x][y]["color"] = color
        self.showPossibleMoves(f"{x}-{y}")

    def start():
        pass


game = Chess()
game.test(3, 3, "king-black", "black")
game.countPieces()


