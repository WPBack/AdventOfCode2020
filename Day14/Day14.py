# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read()

# PART 1: Find the maximum memory location to allocate memory
maxMem = max([int(x) for x in re.findall('\[(\d+)\]', input)])+1

# Create memory and masks
mem = [0]*maxMem
andMask = 2**36-1
orMask  = 0

# Loop over the program and fill in the memory
for line in input.splitlines():
    if line[0:2] == 'ma':
        mask = line[7:]
        for i in range(len(mask)):
            if mask[len(mask)-i-1] == '1':
                andMask |=  (1<<i)
                orMask  |=  (1<<i)

            elif mask[len(mask)-i-1]  == '0':
                andMask &= ~(1<<i)
                orMask  &= ~(1<<i)

            else:
                andMask |=  (1<<i)
                orMask  &= ~(1<<i)

    else:
        memLoc = int(re.search('\[(\d+)\]', line).group(1))
        value = int(re.search('= (\d+)', line).group(1))
        mem[memLoc] = (value & andMask) | orMask

# Calculate the sum of the memory
print('Part 1: ', sum(mem))

# PART 2: Create memory and masks
mem = dict()
andMasks = [2**36-1]
orMasks  = [0]

# Loop over the program and fill in the memory NOT DONE
for line in input.splitlines():
    if line[0:2] == 'ma':
        andMasks = [2**36-1]
        orMasks  = [0]
        mask = line[7:]
        for i in range(len(mask)):
            if mask[len(mask)-i-1] == '1':
                for j in range(len(andMasks)):
                    andMasks[j] |=  (1<<i)
                    orMasks[j]  |=  (1<<i)

            elif mask[len(mask)-i-1]  == '0':
                for j in range(len(andMasks)):
                    andMasks[j] |=  (1<<i)
                    orMasks[j]  &= ~(1<<i)

            else:
                andMasks.extend(andMasks)
                orMasks.extend(orMasks)
                for j in range(len(andMasks)):
                    if j < len(andMasks)/2:
                        andMasks[j] |=  (1<<i)
                        orMasks[j]  |=  (1<<i)
                    else:
                        andMasks[j] &= ~(1<<i)
                        orMasks[j]  &= ~(1<<i)

    else:
        memLoc = int(re.search('\[(\d+)\]', line).group(1))
        value = int(re.search('= (\d+)', line).group(1))
        for i in range(len(andMasks)):
            addr = (memLoc & andMasks[i]) | orMasks[i]
            mem[addr] = value

# Calculate the sum of the memory
print('Part 2: ', sum(mem.values()))