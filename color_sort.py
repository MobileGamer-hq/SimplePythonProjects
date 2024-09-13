import json
import random


#Only able to sort easy and beginner puzzles
class ColorSort:
    current_file = "-beginner"
    num_containers = 9
    file_path = ""

    solution_data = []
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
        self.file_path = path

    def createPuzzle(self):
        self.puzzle = []
        for i in range(self.num_containers):
            self.puzzle.append([])

    def readPuzzle(self):
        print("\nLoading Puzzle Data....")
        path = f"./ColorSort/test-board{self.current_file}.json"
        with open(path, "r") as file:
            data = json.load(file)
            self.num_containers = len(data)
            self.createPuzzle()
            for i in range(self.num_containers):
                for j in range(len(data[i])):
                    self.puzzle[i].append(data[i][len(data[i]) - 1 - j])
        self.file_path = path

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
            elif len(self.puzzle[start]) > 0 and self.puzzle[stop][-1] == self.puzzle[start][-1]:
                self.puzzle[stop].append( self.puzzle[start][-1])
                self.puzzle[start].pop()
            else:
                return None
            print(f"Went from: [{start+1}] to [{stop+1}]")
            self.solution_data.append(f"Went from: [{start+1}] to [{stop+1}]")

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
        # counts[" "] = self.topRow.count(" ")
        # print(counts)

        nums = []
        for i in counts:
            nums.append(counts[i])

        index = nums.index(max(nums))


        
        return list(counts)[index], counts[list(counts)[index]]

    def arrangeEquals(self, equals = []):
        # print("Before Sort:",equals)
        def swap(x, y):
            equals[x], equals[y] = equals[y], equals[x]

        for i in range(len(equals)):
            for j in range(len(equals)):
                if len(self.puzzle[equals[i]]) > len(self.puzzle[equals[j]]):
                    # print(len(self.puzzle[equals[i]]), len(self.puzzle[equals[j]]))
                    swap(i, j)
                

        # print("After Sort:",equals)
        return equals
    
    def findMaxs(self):
        self.seperateIntoLevels()
        counts = {}
        keys = list(self.code_colors.keys())
        for i in keys:
            counts[i] = self.topRow.count(i)
        print(keys)
        print(counts)
        final = []
        for i in counts:
            if counts[i] > 1:
                final.append(self.findAllIndex(i, counts[i]))
        return final


    def findAllIndex(self, value, count):
        _topRow = self.topRow
        ans = []

        def swap(x, y):
            ans[x], ans[y] = ans[y], ans[x]

        
                
        for i in range(count):
            index = _topRow.index(value)
            equals = self.searchEqual(index)
            ans.append({
                "index": index,
                "equals": equals
            })
            _topRow[index] = ""

        for i in range(len(ans)):
            for j in range(len(ans)):
                if len(self.puzzle[ans[i]["index"]]) > len(self.puzzle[ans[j]["index"]]):
                    swap(i, j)

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

    def solve1(self):
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
                    equals = self.arrangeEquals(equals)
                    if len(equals) > 0:
                        for k in equals:
                            if self.checkDone() == False and self.checkFull(k) == False and self.checkRepetition(previous, {"value": max_value, "pos": index}) == False:
                                self.goTo(index, k)
                                previous["pos"], previous["value"]= k, max_value

                                # print(self.possible(index, k))
                                
                                while self.possible(index, k):
                                    # print("Possible")
                                    self.goTo(index, k)
                                    previous["pos"], previous["value"]= k, max_value

                                # done = True
                            elif self.checkDone():
                                break
                            else:
                                continue
                
                self.displayContainers()
                print()
                
                # if self.checkRepetition(previous, {"value": max_value, "pos": index}):
                #     break

            print("Sorted Puzzle")
            self.displayContainers()
            print(f"Moved: {len(self.solution_data)} times")
            path = f"./ColorSort/test-board{self.current_file}-Solution.json"
            print("\nSaving Puzzle Data....")
            with open(path, "w") as file:
                json.dump(self.solution_data, file, indent=4)
            print(f"file saved at: {path}")


    def possible(self, start, stop):
        if self.checkFull(stop) == False and len(self.puzzle[start]) > 0 and self.puzzle[start][-1] == self.puzzle[stop][-1]:
            return True
        else:
            return False

    def solve2(self):
        tries = 1
        for i in range(tries):
            self.readPuzzle()
            self.displayContainers()

            previous = {"value": "", "pos": 0}
            for j in range(3):
            # while self.checkDone() == False:       
                values = self.findMaxs()
                if len(values) > 0:
                    newValues = random.choice(values)

                    for i in newValues:
                        print(i)
                    
        

        
        


puzzle = ColorSort()
# puzzle.inputPuzzle()
# puzzle.readPuzzle()
# puzzle.findMaxs()

# puzzle.displayContainers()
puzzle.solve1()



