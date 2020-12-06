# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Function to decode binary space partitioning
def decodeBinarySpacePartitioning(code, upperChar):
    range = 2**len(code)
    lower = 0
    for c in code:
        range /= 2
        if c == upperChar:
            lower += range

    return int(lower)

# Calculate all seat IDs
seatIds = [decodeBinarySpacePartitioning(seat[:7], 'B') * 8 + decodeBinarySpacePartitioning(seat[-3:], 'R') for seat in input]

# PART 1: Find the max seat ID
print('Part 1: ', max(seatIds))

# PART 2: Find my seat
seatIds.sort()
for i in range(len(seatIds) - 1):
    if(seatIds[i+1] != seatIds[i] + 1):
        print('Part 2: ', seatIds[i] + 1)