# Import modules
import os
import re
import numpy as np
from itertools import compress

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Extract time and bus lines
time = int(input[0])
busLines = [int(bus) for bus in re.findall('\d+', input[1])]

# PART 1: Calculate the waiting time for each bus line
waitTimes = [bus - time%bus for bus in busLines]

# Find the minimum wait time and corresponding line
minWaitTime = min(waitTimes)
minWaitBus = busLines[waitTimes.index(minWaitTime)]

print('Part 1: ', minWaitTime*minWaitBus)

# PART 2: Extract indices for the bus lines
busLinesWithX = input[1].split(',')
busLineIndices = [busLinesWithX.index(str(bus)) for bus in busLines]

timeToMoveToFirstCorrectIndex = [0]*len(busLines)
for i in range(1,len(busLines)):
    time = 0
    while not busLines[i] - time%busLines[i] == busLineIndices[i] and False:
        time += busLines[0]
    
    timeToMoveToFirstCorrectIndex[i] = time

timeToDoFullRotation = np.lcm(busLines[0], busLines)

inSync = [False]*len(busLines)
inSync[0] = True
time = 0
stepLenght = timeToDoFullRotation[0]

while not all(inSync):
    for i in range(len(busLines)):
        if not inSync[i]:
            inSync[i] = busLines[i] - time%busLines[i] == busLineIndices[i]
            stepLength = np.lcm.reduce(list(compress(timeToDoFullRotation, inSync)))
    print(time, inSync, stepLength)
    time += stepLength