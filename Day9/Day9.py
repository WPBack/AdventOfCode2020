# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [int(line) for line in inputFile.read().splitlines()]

# PART 1: Find the first entry that does not follow the rule
for i in range(25, len(input)):
    valid = False
    for j in range(24):
        diff = input[i] - input[i-25+j]
        if (not input[i-25+j] == diff) and diff > 0:
            for k in range(1,25-j):
                if input[i-25+j+k] == diff:
                    valid = True
    if not valid:
        print('Part 1: ', input[i])
        break