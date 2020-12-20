# Import modules
import os
import copy

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [list(line) for line in inputFile.read().splitlines()]

# Function to update the space
def updateSpace(space):
    enlargedSpace = copy.deepcopy(space)

    # Grow the space one step in each axis
    for z in range(len(space)):
        for y in range(len(space[0])):
            enlargedSpace[z][y].append('.')
            enlargedSpace[z][y].insert(0, '.')
    
    for z in range(len(space)):
        enlargedSpace[z].append(['.' for _ in enlargedSpace[0][0]])
        enlargedSpace[z].insert(0, ['.' for _ in enlargedSpace[0][0]])

    enlargedSpace.append([['.' for _ in enlargedSpace[0][0]] for _ in enlargedSpace[0]])
    enlargedSpace.insert(0, [['.' for _ in enlargedSpace[0][0]] for _ in enlargedSpace[0]])

    # Create the new space
    newSpace = copy.deepcopy(enlargedSpace)

    # Loop over the new space and update it
    for z in range(len(newSpace)):
        for y in range(len(newSpace[0])):
            for x in range(len(newSpace[0][0])):
                # Count number of active nearby, including itself
                numActiveNearby = 0
                for checkZ in range(max([z-1,0]), min([z+1,len(newSpace)-1])+1):
                    for checkY in range(max([y-1,0]), min([y+1,len(newSpace[0])-1])+1):
                        for checkX in range(max([x-1,0]), min([x+1,len(newSpace[0][0])-1])+1):
                            if enlargedSpace[checkZ][checkY][checkX] == '#':
                                numActiveNearby += 1
                
                # Update
                if enlargedSpace[z][y][x] == '#' and not (numActiveNearby == 3 or numActiveNearby == 4):
                    newSpace[z][y][x] = '.'

                elif enlargedSpace[z][y][x] == '.' and numActiveNearby == 3:
                    newSpace[z][y][x] = '#'

    return newSpace

# PART 1: Update the space 6 times
space = [input]
for i in range(6):
    space = updateSpace(space)

# Count the number of active
numActive = 0
for z in range(len(space)):
        for y in range(len(space[0])):
            for x in range(len(space[0][0])):
                if space[z][y][x] == '#':
                    numActive += 1

print('Part 1: ', numActive)