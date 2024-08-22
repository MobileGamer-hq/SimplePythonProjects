import datetime
import random
import math
import time

def getBirthdays(times):
    months = (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    )

    birthdays = []
    
    for i in range(times):
        day = datetime.date(2001, 1, 1) + datetime.timedelta(random.randint(0,364))
        month = months[day.month - 1]

        birthday = f"{month} {day.day}"
        birthdays.append(birthday)

    return birthdays

def contains(_list, value):
    for i in _list:
        if i == value:
            return True
    return False

def getMatches(birthdays):
    seen = []
    duplicates = []
    for day in birthdays:
        if len(seen) > 0:
            if contains(seen, day) == True:
                duplicates.append(day)
            else:
                seen.append(day)
        else:
            seen.append(day)
    return duplicates


def start(num):
    print("Starting")

    value = 0
    for i in range(num):
        birthdays = getBirthdays(23)
        matches = getMatches(birthdays)
        value += len(matches)
        if i == 0:
            print("FIRST TEST RAN")
            print(f"Birthdays: {birthdays}\nMultiple people had a birthday on: {matches}")
            time.sleep(10)
        elif i == math.floor(num/4):
            print("Quarter WAY THERE")
            print(f"Simulations: {i}\nMatches: {value}")
        elif i == num/2:
            print("Half WAY THERE")
            print(f"Simulations: {i}\nMatches: {value}")

    print("DONE!!!")
    print(f"WE GOT {value} MATCHES OUT OF {num} NUMBER OF SIMULATIONS")
    print(f"{(value/num) * 100}% probability of getting a match")

start(100_000)