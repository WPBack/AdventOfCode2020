# Import modules
import os
import copy

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [list(line) for line in inputFile.read().splitlines()]

# Function to update the map
def updateMap(map):
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
    (changed, map) = updateMap(map)

# PART 1: Count the number of occuiped seats
numOccupied = 0
for row in map:
    numOccupied += row.count('#')

print('Part 1: ', numOccupied)