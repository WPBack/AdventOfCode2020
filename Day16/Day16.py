# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Field class
class Field:
    def __init__(self, fieldString):
        filteredString = re.match('([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', fieldString)
        self.name       = filteredString.group(1)
        self.lowLim1    = int(filteredString.group(2))
        self.highLim1   = int(filteredString.group(3))
        self.lowLim2    = int(filteredString.group(4))
        self.highLim2   = int(filteredString.group(5))

    def __withinLim1(self, num):
        return num >= self.lowLim1 and num <=self.highLim1

    def __withinLim2(self, num):
        return num >= self.lowLim2 and num <=self.highLim2

    def withinLimits(self, num):
        return self.__withinLim1(num) or self.__withinLim2(num)

# Create the field objects
fields = [Field(fieldString) for fieldString in input[:20]]

# Create list of nearby tickets
nearbyTickets = [ticket.split(',') for ticket in input[25:]]
for i in range(len(nearbyTickets)):
    nearbyTickets[i] = [int(num) for num in nearbyTickets[i]]

# PART 1: Fin all invalid fields and sum them upp
ticketScanningErrorRate = 0
for ticket in nearbyTickets:
    for num in ticket:
        valid = False
        for field in fields:
            if field.withinLimits(num):
                valid = True
        if not valid:
            ticketScanningErrorRate += num

print('Part 1: ', ticketScanningErrorRate)
