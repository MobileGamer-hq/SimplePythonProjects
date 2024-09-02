import random
import time
from datetime import datetime
import json

def createCards():


    cards = []
    shapes = {"spades": chr(9824), "clubs": chr(9827), "hearts" : chr(9829), "diamonds" : chr(9830)}

    for shape in shapes:
        for i in range(14):
            newCard  = {
                "shape": None,
                "value": None,
                "color": None
            }
            if i == 0:
                continue
            elif i == 1:
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
            if shape == "spades" or shape == "clubs":
                newCard["color"] = "black"
            else:
                newCard["color"] = "red"
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
    newDeck.append({
                "shape": ">",
                "value": ">"
            })
    print("\n  [7]    [8]  ")
    displayCardRow(newDeck)
    #print("\nThis is your Deck")

    #Draw Top Row
    indexs = ""
    for i in range(4):
        if i + 8 < 10:
            indexs += f"  [{i + 9}]  "
        else:
            indexs += f"  [{i + 9}] "
    
    if len(topRow) < 4:
        for i in range(4 - len(topRow)):
            topRow.append({
                "shape": "#",
                "value": "#"
            })
    print(f"\n{indexs}")
    displayCardRow(topRow)


def convert(value):
    match value:
        case "J":
            return "11"
        case "Q":
            return "12"
        case "K":
            return "13"
        case "A":
            return "0"
        case _:
            return value
        

def checkCardsMatch(card1, card2, colorMatters = False):


    if colorMatters:
        if int(convert(card1["value"])) == int(convert(card2["value"])) - 1 and card1["color"] is not card2["color"] :
            return True
    else:
        if int(convert(card1["value"])) == int(convert(card2["value"])) - 1 and card1["shape"] is card2["shape"]:
            return True
    return False
    

def createGame(cards, _range = 7):
    prev = 0
    columns = [[],[],[],[],[],[],[]]
    for i in range(_range):
        for i in range(i + 1):
            columns[i].append(cards[i])
        for i in range(i + 1):
            cards.remove(cards[0])

    return columns


def saveData(table):
    print("\nSaving Board Data....")
    cureentTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    location = f"./Solitaire/{cureentTime}.json"
    with open(location, "w") as file:
        json.dump(table, file, indent=4)
    time.sleep(2)
    print(f"Saved Board Data To: {location}")


def start():
    cards = createCards()
    random.shuffle(cards)
    columns = createGame(cards)
    columns.reverse()

    topRow = []
    deck = cards.copy()

    while True:
        drawTable(columns, topRow, deck)

        while True:
            command = input("\nEnter your command: ")
            print(f"You selected [{command}]")

            

            if command == "8":
                random.shuffle(deck)
                print("Shuffling...")
                #time.sleep(2)
                break
            elif int(command) > 8:
                print("You can't pick that command now")
                continue
            elif int(command) < 8:
                second_command = input("\nEnter your second command: ")
                if int(command) < 7 and int(second_command) < 7:
                    match = checkCardsMatch(columns[int(command)][-1], columns[int(second_command)][-1], True)
                    if match:
                        columns[int(second_command)].append(columns[int(command)][-1])
                        columns[int(command)].remove(columns[int(command)][-1])
                        break
                    else:
                        print("Action not allowed they do not match")

                elif command == "7" and int(second_command) < 7:
                    match = checkCardsMatch(deck[-1], columns[int(second_command)][-1], True)
                    if match:
                        columns[int(second_command)].append(deck[-1])
                        deck.remove(deck[-1])
                        break
                    else:
                        print("Action not allowed, they do not match")

                elif int(command) < 7 and int(second_command) > 8:
                    if columns[int(command)][-1]["value"] == "A":
                        topRow[int(second_command) - 9] = columns[int(command)][-1]
                        columns[int(command)].remove(columns[int(command)][-1])
                        break
                    else:
                        match = checkCardsMatch(columns[int(command)][-1], topRow[int(second_command) - 9])
                        if match:
                            topRow[int(second_command) - 9] = columns[int(command)][-1]
                            columns[int(command)].remove(columns[int(command)][-1])
                            break
                        else:
                            print("Action not allowed they do not match")

                elif command == "7" and int(second_command) > 8:
                    if deck[-1]["value"] == "A":
                        topRow[int(second_command) - 9] = deck[-1]
                        deck.remove(deck[-1])
                        break
                    else:
                        match = checkCardsMatch(deck[-1], topRow[int(second_command) - 9])
                        if match:
                            topRow[int(second_command) - 9] = columns[int(command)][-1]
                            deck.remove(deck[-1])
                            break
                        else:
                            print("Action not allowed they do not match")
            
        saveData({"columns": columns, "top-row": topRow, "deck": deck})

                
                


start()
