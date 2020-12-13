# Import modules
import os
import re

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
maxBusLine = max(busLines)

time = maxBusLine - busLineIndices[busLines.index(maxBusLine)]
while not (all([(busLines[i] - time%busLines[i]) == busLineIndices[i] for i in range(1,len(busLines))]) and time%busLines[0] == 0):
    time += maxBusLine
    print(time)

print('Part 2: ', time)