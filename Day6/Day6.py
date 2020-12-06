# Import modules
import os

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().split("\n\n")

# PART 1: Count the number of yes answers for each and sum up
answers = input.copy()
for i in range(len(input)):
    answers[i] = input[i].replace('\n', '')

numYes = 0
for answer in answers:
    numYes += len(set(answer))

print('Part 1: ', numYes)

# PART 2: Count the number where all in one group answered yes
answers = [group.splitlines() for group in input]
numYes = 0
for group in answers:
    groupSets = [set(answer) for answer in group]
    numYes += len(set.intersection(*groupSets))

print('Part 2: ', numYes)