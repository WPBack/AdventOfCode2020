# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Bag class
class Bag:
    def __init__(self, bagString):
        self.color = re.search('([^\s]+\s+[^\s]+)', bagString).group(0)
        childStrings = re.findall('(\d)\s([^\s]+\s[^\s]+)', bagString)
        self.childBagNums = [i[0] for i in childStrings]
        self.childBagColors = [i[1] for i in childStrings]
        self.children = []

    def buildChildren(self, bagList):
        for childColor in self.childBagColors:
            for bag in bagList:
                if bag.color == childColor:
                    self.children.append(bag)
    
    def getAllChildren(self):
        result = []
        if not self.children:
            return []
        else:
            for child in self.children:
                result.append(child)
                result.extend(child.getAllChildren())
        return result

# Create list of bags
bags = [Bag(bagString) for bagString in input]

for bag in bags:
    bag.buildChildren(bags)

# PART 1: Loop over the list of bags and count which eventually holds a shiny gold bag
numShinyGold = 0

for bag in bags:
    containsShinyGold = False
    children = bag.getAllChildren()
    for child in children:
        if child.color == 'shiny gold':
            containsShinyGold = True
    if containsShinyGold:
        numShinyGold += 1

print('Part 1: ', numShinyGold)