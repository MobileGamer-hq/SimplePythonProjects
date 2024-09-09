import json
import random


#Only able to sort easy and beginner puzzles
class ColorSort:
    current_file = "-easy"
    num_containers = 4
    def __init__(self) -> None:
        self.puzzle = []
        self.levels = []
        self.topRow = []
        pass

    colors_code = {
        #
        "blue": "B",
        "red": "R",
        "green": "G",
        "yellow": "Y",
        "pink": "P",
        "violet": "V",
        "orange": "O",
        "white": "W",
        "Amber": "A",
    }

    code_colors = {
        #
        "B": "blue",
        "R": "red",
        "G": "green",
        "Y": "yellow",
        "P": "pink",
        "V": "violet",
        "O": "ornage",
        "W": "white",
        "A": "amber"
    }



    def inputPuzzle(self):
        print(self.code_colors)
        puzzle = []
        self.num_containers = int(input("Enter the number of containers in the puzzle: "))
        for i in range(self.num_containers):
            container = input(f"colors in container [{i + 1}]: ")
            puzzle.append(container)
        path = f"./ColorSort/test-board{self.current_file}.json"
        print("\nSaving Puzzle Data....")
        with open(path, "w") as file:
            json.dump(puzzle, file, indent=4)
        print(f"file saved at: {path}")

    def createPuzzle(self):
        self.puzzle = []
        for i in range(self.num_containers):
            self.puzzle.append([])

    def readPuzzle(self):
        self.createPuzzle()
        print("\nLoading Puzzle Data....")
        path = f"./ColorSort/test-board{self.current_file}.json"
        with open(path, "r") as file:
            data = json.load(file)
            for i in range(self.num_containers):
                for j in range(len(data[i])):
                    self.puzzle[i].append(data[i][len(data[i]) - 1 - j])

    def displayContainers(self):
        count = 0
        for container in self.puzzle:
            count += 1
            print(f"{count}:", container)
    
    def goTo(self, start, stop):
        if self.checkFull(stop):
            return None
        else:
            if len(self.puzzle[stop]) == 0:
                self.puzzle[stop].append( self.puzzle[start][-1])
                self.puzzle[start].pop()
            elif self.puzzle[stop][-1] == self.puzzle[start][-1]:
                self.puzzle[stop].append( self.puzzle[start][-1])
                self.puzzle[start].pop()
            else:
                return None
            print(f"Went from: [{start+1}] to [{stop+1}]")

    def seperateIntoLevels(self):
        self.levels = [[], [], [], []]
        self.topRow = []
        for i in range(4):
            for container in self.puzzle:
                if len(container) > i:
                    self.levels[i].append(container[i])
                else:
                    self.levels[i].append(" ")

        for container in (self.puzzle):
            if len(container) > 0:
                self.topRow.append(container[-1])
            else:
                self.topRow.append(" ")

        return self.levels

    def searchEqual(self, index):
        equals = []
        for i in range(self.num_containers):
            if i != index and len(self.puzzle[index]) > 0:
                if len(self.puzzle[i]) > 0:
                    if self.puzzle[i][-1] == self.puzzle[index][-1]:
                        equals.append(i)
                else:
                    equals.append(i)
        return equals

    def findMax(self):
        self.seperateIntoLevels()
        counts = {}
        keys = list(self.code_colors.keys())
        random.shuffle(keys)
        for i in keys:
            counts[i] = self.topRow.count(i)
        counts[" "] = self.topRow.count(" ")
        # print(counts)

        nums = []
        for i in counts:
            nums.append(counts[i])

        index = nums.index(max(nums))
        
        return list(counts)[index], counts[list(counts)[index]]

    def findAllIndex(self, value, count):
        _topRow = self.topRow
        ans = []
                
        for i in range(count):
            index = _topRow.index(value)
            equals = self.searchEqual(index)
            ans.append({
                "index": index,
                "equals": equals
            })
            _topRow[index] = ""

        return ans

    def checkDone(self):
        done_count = 0
        for container in self.puzzle:
            if len(container) > 0:
                count = container.count(container[0])

                if count == 4:
                    done_count += 1
            else:
                done_count += 1

        if done_count == len(self.puzzle):
            return True
        else:
            return False
        
    def checkFull(self, container):
        if len(self.puzzle[container]) < 4: 
            return False
        else:
            return True

    def checkRepetition(self, previous, present):
        if previous["value"] == present["value"] and previous["pos"] == present["pos"]:
            return True
        return False

    def solve(self):
        tries = 1
        for i in range(tries):
            self.readPuzzle()
            self.displayContainers()

            previous = {"value": "", "pos": 0}
            # for j in range(self.num_containers**self.num_containers):
            while self.checkDone() == False:
                max_value, count = self.findMax()

                values = self.findAllIndex(max_value, count)
                
                for value in values:
                    
                    index = value["index"]
                    equals = value["equals"]

                    

                    # print(max_value, count, index, equals)
                    
                    # done = False
                    if len(equals) > 0:
                        for k in equals:
                            if self.checkFull(k) == False and self.checkRepetition(previous, {"value": max_value, "pos": index}) == False:
                                self.goTo(index, k)
                                previous["pos"], previous["value"]= k, max_value
                                
                                # done = True
                            else:
                                continue
                
                self.displayContainers()
                print()
                
                # if self.checkRepetition(previous, {"value": max_value, "pos": index}):
                #     break

            print("Sorted Puzzle")
            self.displayContainers()
                
            
                    
        

        
        


puzzle = ColorSort()
# puzzle.readPuzzle()
# puzzle.inputPuzzle()
# puzzle.displayContainers()
puzzle.solve()

