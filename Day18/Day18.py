# Import modules
import os
import regex

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Recursive function to evaluate an expression
def evalExp(exp):
    parts = regex.finditer('(\+)|(\*)|(\d)|\((([^\)\(]+)|(?R))*+\)', exp)
    operands = []
    operators = []

    for part in parts:
        if part.group(0) == '+':
            operators.append(part.group(0))
        elif part.group(0) == '*':
            operators.append(part.group(0))
        elif part.group(0)[0] == '(':
            operands.append(part.group(0)[1:-1])
        else:
            operands.append(part.group(0))

    if not operators:
        if len(operands[0]) == 1:
            return int(operands[0])
        else:
            return evalExp(operands[0])

    else:
        result = evalExp(operands[0])
        for i in range(len(operators)):
            if operators[i] == '+':
                result += evalExp(operands[i+1])
            else:
                result *= evalExp(operands[i+1])

        return result

# Evaluate all expressions
results = [evalExp(exp) for exp in input]

# PART 1: Sum all the results
print('Part 1: ', sum(results))