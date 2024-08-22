import random

def createCards():


    cards = []
    shapes = {"spades": chr(9824), "clubs": chr(9827), "hearts" : chr(9829), "diamonds" : chr(9830)}

    for shape in shapes:
        for i in range(14):
            newCard  = {
                "shape": None,
                "value": None
            }
            if i == 0:
                newCard["value"] = "A"
            elif i == 11:
                newCard["value"] = "J"
            elif i == 12:
                newCard["value"] = "Q"
            elif i == 13:
                newCard["value"] = "K"
            else:
                newCard["value"] = str(i)
            newCard["shape"] = shapes[shape]
            cards.append(newCard)

    return cards
    
def displayCardRow(cards):
    levels = ["","","",""]
    for card in cards:
        if card["value"] == "10":
            levels[0] += "  ___  "
            levels[1] += f" |{card["value"]} | "
            levels[2] += f" | {card["shape"]} | "
            levels[3] += f" |_{card["value"]}| "
        else:
            levels[0] += "  ___  "
            levels[1] += f" |{card["value"]}  | "
            levels[2] += f" | {card["shape"]} | "
            levels[3] += f" |__{card["value"]}| "
    
    for i in levels:
        print(i)
        

def drawTable(columns, topRow, deck):
    
    #Draw Columns 
    showingRow = []
    showingCount = ""
    indexs = ""
    x = 0
    for i in columns:
        showingRow.append(i[len(i) - 1])
        showingCount += f"   {len(i)}   "
        indexs += f"  [{x}]  "
        x += 1
    
    print(indexs)
    displayCardRow(showingRow)
    print(f"\n{showingCount}")

    #Draw Deck
    newDeck = []
    newDeck.append(deck[-1])
    print("\n  [7]")
    displayCardRow(newDeck)
    print("\nThis is your Deck")

    #Draw Top Row
    indexs = ""
    for i in range(4):
        if i + 8 < 10:
            indexs += f"  [{i + 8}]  "
        else:
            indexs += f"  [{i + 8}] "
    
    if len(topRow) == 0:
        for i in range(4):
            topRow.append({
                "shape": "#",
                "value": "#"
            })
    print(f"\n{indexs}")
    displayCardRow(topRow)

def createGame(cards, _range = 7):
    prev = 0
    columns = [[],[],[],[],[],[],[]]
    for i in range(_range):
        for i in range(i + 1):
            columns[i].append(cards[i])
        for i in range(i + 1):
            cards.remove(cards[0])

    return columns


def start():
    cards = createCards()
    random.shuffle(cards)
    columns = createGame(cards)
    columns.reverse()

    topRow = []
    deck = cards.copy()

    drawTable(columns, topRow, deck)

    command = input("\nEnter your command: ")

    
    


start()
