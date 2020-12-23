# Import modules
import os
import regex

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# PART 1: Recursive function to evaluate an expression
def evalExpPart1(exp):
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
            return evalExpPart1(operands[0])

    else:
        result = evalExpPart1(operands[0])
        for i in range(len(operators)):
            if operators[i] == '+':
                result += evalExpPart1(operands[i+1])
            else:
                result *= evalExpPart1(operands[i+1])

        return result

# Evaluate all expressions
results = [evalExpPart1(exp) for exp in input]

# Sum all the results
print('Part 1: ', sum(results))

# PART 2: Recursive function to evaluate an expression
def evalExpPart2(exp):
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
            return evalExpPart2(operands[0])

    else:
        if '*' in operators:
            mulPos = operators.index('*')
            leftExp = ''
            rightExp = ''

            if mulPos == 0:
                leftExp = operands[0]
            else:
                for i in range(mulPos):
                    leftExp += '(' + operands[i] + ') ' + operators[i] + ' '
                leftExp += '(' + operands[i+1] + ')'

            if mulPos == len(operators) - 1:
                rightExp = operands[-1]
            else:
                for i in range(mulPos+1, len(operators)):
                    rightExp += '(' + operands[i] + ') '  + operators[i] + ' '
                rightExp += '(' + operands[i+1] + ')'

            return evalExpPart2(leftExp) * evalExpPart2(rightExp)
        
        else:
            result = evalExpPart2(operands[0])
            for i in range(len(operators)):
                result += evalExpPart2(operands[i+1])
            
            return result


# Evaluate all expressions
results = [evalExpPart2(exp) for exp in input]

# Sum all the results
print('Part 2: ', sum(results))