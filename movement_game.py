boundaries = 20

def generateData(rows, columns):
    squares = []
    

    for i in range(rows):
        row = []
        for j in range(columns):
            square = f"{i}-{j}"
            row.append({
                "value": "",
                "square": square,
                "empty": True
            })
        squares.append(row)

    return squares

    



def drawWindow(data):
    for i in range(boundaries):
        line = ""
        for j in range(boundaries):
            if data[i][j]["value"] == "":
                line += "[ ]"
            else: 
                line += f"[{data[i][j]["value"]}]"
        print(line)

    print("\n")

class Character:
    sprites = [chr(164), chr(8226), chr(9679), chr(9675), chr(9650)]
    sprite = str(sprites[0])
    pos = {"row": 0, "column": 0}

    def __init__(self, _sprite, _speed, squares) -> None:
        self.sprite = str(self.sprites[_sprite])
        self.speed = _speed
        squares[self.pos["row"]][self.pos["column"]]["value"] = self.sprite
        


    def move(self, squares ):
        direction = input(": ")

        squares[self.pos["row"]][self.pos["column"]]["value"] = ""
        match direction:
            case ">":
                
                self.pos["column"] += self.checkSpeed("column")
            case "<":
                self.pos["column"] -= self.checkSpeed("column")
            case "_":
                self.pos["row"] -= self.checkSpeed("row")
            case "^":
                self.pos["row"] += self.checkSpeed("row")
            case _:
                pass

        squares[self.pos["row"]][self.pos["column"]]["value"] = self.sprite
        drawWindow(squares)
        # print(self.pos)

    def checkSpeed(self, dir):
        if self.speed + self.pos[dir] > boundaries:
            return boundaries - self.pos[dir]
        else:
            return self.speed

        


def start():
    squares = generateData(boundaries, boundaries)
    character = Character(0, 3, squares)
    
    while True:
        drawWindow(squares)
        character.move(squares)

start()


