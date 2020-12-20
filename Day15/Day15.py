# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [int(num) for num in inputFile.read().split(',')]

# Create a dictionary of the spoken numbers
spoken = dict()

# Fill in the dictionary with the starting numbers
lastSpoken = 0
firstTime = True
for i in range(len(input)):
    lastSpoken = input[i]
    firstTime = not (lastSpoken in spoken)
    if not firstTime:
        lastTurnSpoken = spoken[lastSpoken]
    spoken[lastSpoken] = i+1

# PART 1: Loop until the 2020th number is spoken
for i in range(len(input)+1, 2021):
    if firstTime:
        lastSpoken = 0
    else:
        lastSpoken = i-1 - lastTurnSpoken

    firstTime = not (lastSpoken in spoken)
    if not firstTime:
        lastTurnSpoken = spoken[lastSpoken]

    spoken[lastSpoken] = i

print('Part 1: ', lastSpoken)

# Part 2: Keep on going until the 30000000th number is spoken

for i in range(2021, 30000001):
    if firstTime:
        lastSpoken = 0
    else:
        lastSpoken = i-1 - lastTurnSpoken

    firstTime = not (lastSpoken in spoken)
    if not firstTime:
        lastTurnSpoken = spoken[lastSpoken]

    spoken[lastSpoken] = i

print('Part 2: ', lastSpoken)