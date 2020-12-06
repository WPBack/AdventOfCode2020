# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines() 

# Convert input into boolean map where true represents a tree
map = [[False]*len(input) for i in range(len(input[0]))]
for x in range(len(input[0])):
    for y in range(len(input)):
        if input[y][x] == '#':
            map[x][y] = True

# PART 1: Count how may trees you encounter if you go 3 left for each 1 down
numTrees = 0
x = 0
for y in range(len(map[0])):
    if map[x%len(map)][y]:
        numTrees += 1
    x += 3

print('Part 1: ', numTrees)

# PART 2: Function to count number of trees for arbitrary slope
def countTrees(map, dx, dy):
    numTrees = 0
    x = 0
    for y in range(0, len(map[0]), dy):
        if map[x%len(map)][y]:
            numTrees += 1
        x += dx
    return numTrees

print('Part 2: ', countTrees(map, 1, 1)*\
                  countTrees(map, 3, 1)*\
                  countTrees(map, 5, 1)*\
                  countTrees(map, 7, 1)*\
                  countTrees(map, 1, 2))