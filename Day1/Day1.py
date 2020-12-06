# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [int(i) for i in inputFile.readlines()]

# Find two entries that sum up to 2020 by trial and error
for i in input:
    for j in input[i:]:
        if i + j == 2020:
            print('Part 1: ',i*j)

# Find three entries that sum up to 2020 by trial and error
for i in input:
    for j in input:
        for k in input:
            if i + j + k == 2020:
                print('Part 2: ',i*j*k)
