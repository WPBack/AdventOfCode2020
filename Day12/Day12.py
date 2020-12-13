# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Extract actions and values
actions = [instr[0] for instr in input]
values = [int(instr[1:]) for instr in input]

# Find the destination
x = 0
y = 0
dir = 90

for i in range(len(actions)):
    if actions[i] == 'N':
        y += values[i]

    elif actions[i] == 'S':
        y -= values[i]

    elif actions[i] == 'E':
        x += values[i]

    elif actions[i] == 'W':
        x -= values[i]

    elif actions[i] == 'L':
        dir -= values[i]

    elif actions[i] == 'R':
        dir += values[i]

    elif actions[i] == 'F':
        if dir % 360 == 0:
            y += values[i]
        elif dir % 360 == 90:
            x += values[i]
        elif dir % 360 == 180:
            y -= values[i]
        elif dir % 360 == 270:
            x -= values[i]

# PART 1; Calculate the Nabhattan distance
print('Part 1: ', abs(x) + abs(y))