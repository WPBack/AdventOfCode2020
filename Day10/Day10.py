# Import modules
import os
import numpy as np
from math import comb

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [int(line) for line in inputFile.read().splitlines()]

# Sort the list
input.sort()

# Add device adapter and wall joltage
input.append(input[-1]+3) 
input.insert(0,0)

# PART 1: Count the difference between each adapter
diff = np.diff(input).tolist()

print('Part 1: ', diff.count(1)*diff.count(3))

# PART 2: Count how many ways the joltage can be achieved
print(input)
print(diff)
numCombinations = 1
numOnesInOrder = 0
for i in range(len(diff)):
    if diff[i] == 1:
        numOnesInOrder += 1
    else:
        if numOnesInOrder > 1:
            currNumCombs = 0
            for j in range(numOnesInOrder):
                if not (j == 0 and numOnesInOrder > 3):
                    currNumCombs += comb(numOnesInOrder-1, j)
            numCombinations *= currNumCombs
        numOnesInOrder = 0

print('Part 2: ', numCombinations)