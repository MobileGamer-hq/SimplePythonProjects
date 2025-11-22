import random
from collections import deque
from os.path import getsize

maze = []
size = 5

def createMaze(size, num):
    for i in range(size):
        row = []
        for j in range(size):
            row.append("0")
        maze.append(row)

    for i in range(num):
        x = random.choice(list(range(size)))
        y = random.choice(list(range(size)))

        maze[x][y] = "#"



def displayMaze(maze):
    for row in maze:
        print(row)
    print()

createMaze(5, 10)
displayMaze(maze)

def getNeighbors(x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or x + i >= 5 or y + j < 0 or y + j >= 5:
                continue
            if maze[x + i][y + j] != "#":
                neighbors.append((x + i, y + j))
    return neighbors

def getSize(_x, _y):
    _size = 0
    for i in range(-1,2 ):
        for j in range(-1,2 ):
            if _x+i < 0 or _x+i > 4 or _y+j < 0 or _y+j > 4:
                continue
            if i == 0 and j == 0:
                continue
            if maze[_x+i][_y + j] != "#":
                # print(f"Value at {_x+i}-{_y+j} is: ", maze[_x+i][_y + j])
                _size += 1

    return _size


visited = set()
queue = deque([(0,0)])

while len(queue) > 0:
    x, y = queue.popleft()
    if (x, y) in visited: continue
    value = maze[x][y]
    visited.add((x, y))
    if value == "#":
        for pos in getNeighbors(x, y):
            queue.append((pos[0], pos[1]))
    else:
        maze[x][y] = str(getSize(x, y))
        for pos in getNeighbors(x, y):
            queue.append((pos[0], pos[1]))


displayMaze(maze)

