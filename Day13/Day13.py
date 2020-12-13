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

# Calculate the waiting time for each bus line
waitTimes = [bus - time%bus for bus in busLines]

# Find the minimum wait time and corresponding line
minWaitTime = min(waitTimes)
minWaitBus = busLines[waitTimes.index(minWaitTime)]

# PART 1: Multiply the wait time with the bus line
print('Part 1: ', minWaitTime*minWaitBus)