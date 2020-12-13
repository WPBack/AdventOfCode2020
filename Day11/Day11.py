# Import modules
import os
import copy

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [list(line) for line in inputFile.read().splitlines()]

# PART 1: Function to update the map
def updateMapPart1(map):
    changed = False
    newMap = copy.deepcopy(map)
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 'L':
                getsOccupied = True
                for checkRow in range(max([row-1,0]), min([row+1,len(map)-1])+1):
                    for checkCol in range(max([col-1,0]), min([col+1,len(map[0])-1])+1):
                        if map[checkRow][checkCol] == '#':
                            getsOccupied = False
                if getsOccupied:
                    newMap[row][col] = '#'
                    changed = True

            elif map[row][col] == '#':
                numOccupiedNear = 0
                for checkRow in range(max([row-1,0]), min([row+1,len(map)-1])+1):
                    for checkCol in range(max([col-1,0]), min([col+1,len(map[0])-1])+1):
                        if (map[checkRow][checkCol] == '#') and not (checkRow == row and checkCol == col):
                            numOccupiedNear += 1
                if numOccupiedNear >= 4:
                    newMap[row][col] = 'L'
                    changed = True
    return (changed, newMap)

# Update the map until it gets full
map = copy.deepcopy(input)
changed = True
while changed:
    (changed, map) = updateMapPart1(map)

# Count the number of occuiped seats
numOccupied = 0
for row in map:
    numOccupied += row.count('#')

print('Part 1: ', numOccupied)

# PART 2: Function to check the first seat in a given direction
def firstSeat(map, row, col, drow, dcol):
    checkRow = row + drow
    checkCol = col + dcol
    while checkRow >= 0 and checkRow < len(map) and checkCol >= 0 and checkCol < len(map[0]):
        if not map[checkRow][checkCol] == '.':
            return map[checkRow][checkCol]
        else:
            checkRow += drow
            checkCol += dcol
    
    return '.'

# Function to count number of occupied first seats
def numOccupiedFirst(map, row, col):
    return [firstSeat(map, row, col, 1, 0), firstSeat(map, row, col, 1, 1), firstSeat(map, row, col, 0, 1), firstSeat(map, row, col, -1, 1), firstSeat(map, row, col, -1, 0), firstSeat(map, row, col, -1, -1), firstSeat(map, row, col, 0, -1), firstSeat(map, row, col, 1, -1)].count('#')
    

# Function to update the map
def updateMapPart2(map):
    changed = False
    newMap = copy.deepcopy(map)
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 'L':
                if numOccupiedFirst(map, row, col) == 0:
                    newMap[row][col] = '#'
                    changed = True

            elif map[row][col] == '#':
                if numOccupiedFirst(map, row, col) >= 5:
                    newMap[row][col] = 'L'
                    changed = True
    return (changed, newMap)

# Update the map until it gets full
map = copy.deepcopy(input)
changed = True
while changed:
    (changed, map) = updateMapPart2(map)

# Count the number of occuiped seats
numOccupied = 0
for row in map:
    numOccupied += row.count('#')

print('Part 2: ', numOccupied)