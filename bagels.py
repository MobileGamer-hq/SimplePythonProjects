import random

maxNum = 3

def getNumber():
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    randomNumber = ""
    while len(randomNumber) < maxNum:
        selected = random.choice(numbers)
        randomNumber += selected
        numbers.remove(selected)

    return randomNumber

def checkNumber(number, randomNumber):
    clues = []

    if len(number) < maxNum:
        return f"Your number is less than the max num of values: {maxNum}"
    elif len(number) > maxNum:
        return f"Your number is greater than the max num of values: {maxNum}"
    
    if number == randomNumber:
        return "You won!, your number is correct."

    for i in range(len(number)):
        if number[i] == randomNumber[i]:
            clues.append("Pico")
        elif number[i] in randomNumber:
            clues.append("Fermi")
    
    if len(clues) == 0:
        return "Bagels"
    return str(clues)


def start():
    numGuess = 10
    print(f"""
Welcome to the Bagel, today your going to be guessig a randome 3 digit numebr.
numbers can not be repeated.
numbers can not have more than or less than the max num of values {maxNum}
You have only {numGuess} guesses
you will be getting this clues:
Pico: One digit is correct and in the right place
Fermi: one digi is correct but in the wrong place
Bageld: No digit is correct

to stop type 'stop'.
Have fun!!!
""")
    while True:
        randomNumber = getNumber()
        for i in range(numGuess):
            guess = input(f"Guess #{i + 1}: ")
            response = checkNumber(guess, randomNumber)

            if response == "You won!, your number is correct.":
                print(response)
                break
            print(response)
            continue
        response = input("Do you want to play again 'Yes' or 'No'")
        if response.lower() == "yes":
            continue
        else:
            print("Okay, Bye")
            break
            
    

start()
