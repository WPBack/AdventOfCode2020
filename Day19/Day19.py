# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().split('\n\n')

# Sort the rules and strip the numbers
rules = [row.split(': ') for row in input[0].splitlines()]
rules = [[int(row[0]), row[1]] for row in rules]
rules = [row[1] for row in sorted(rules)]

# Recursive function to build a regex string from a rule
def buildRule(ruleId, rules):
    rule = rules[ruleId]

    if rule[0] == '\"':
        return rule[1]

    else:
        rule = rule.split(' ')
        result = '('
        for part in rule:
            if part == '|':
                result += '|'
            else:
                result += buildRule(int(part), rules)

        result += ')'
        return result

# Build rule 0
rule0str = buildRule(0, rules)
rule0re = re.compile(rule0str)

# PART 1: Check how many messages fully match the rule 0
numFullMatch = 0

for message in input[1].splitlines():
    match = rule0re.match(message)
    if match:
        if match.group(0) == message:
            numFullMatch += 1

print('Part 1: ', numFullMatch)