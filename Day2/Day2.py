# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = [re.match('(\d+)-(\d+) (\w): (\w+)', i) for i in inputFile.readlines()]


# Count number of valid passwords according to policy 1
validPasswords = 0
for i in input:
    numChars = 0
    for c in i.group(4):
        if c == i.group(3):
            numChars += 1
    if numChars >= int(i.group(1)) and numChars <= int(i.group(2)):
        validPasswords += 1

print('Part 1: ', validPasswords)

# Count number of valid passwords accoring to policy 2
validPasswords = 0
for i in input:
    if (i.group(4)[int(i.group(1))-1] == i.group(3) and i.group(4)[int(i.group(2))-1] != i.group(3)) or (i.group(4)[int(i.group(1))-1] != i.group(3) and i.group(4)[int(i.group(2))-1] == i.group(3)):
        validPasswords += 1

print('Part 2: ', validPasswords)