# Import modules
import os
import numpy as np

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