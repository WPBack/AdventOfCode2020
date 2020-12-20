# Import modules
import os
import re
import numpy as np

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

        self.location = -1

    def __withinLim1(self, num):
        return num >= self.lowLim1 and num <=self.highLim1

    def __withinLim2(self, num):
        return num >= self.lowLim2 and num <=self.highLim2

    def withinLimits(self, num):
        return self.__withinLim1(num) or self.__withinLim2(num)

# Create the field objects
fields = [Field(fieldString) for fieldString in input[:20]]
#fields = [Field(fieldString) for fieldString in input[:3]]

# Create list of nearby tickets
nearbyTickets = [ticket.split(',') for ticket in input[25:]]
#nearbyTickets = [ticket.split(',') for ticket in input[8:]]
for i in range(len(nearbyTickets)):
    nearbyTickets[i] = [int(num) for num in nearbyTickets[i]]

# Find all invalid fields, sum them upp and save the indices of the invalid tickets
invalidTickets = []
ticketScanningErrorRate = 0
for i in range(len(nearbyTickets)):
    for num in nearbyTickets[i]:
        valid = False
        for field in fields:
            if field.withinLimits(num):
                valid = True
        if not valid:
            invalidTickets.append(i)
            ticketScanningErrorRate += num

# PART 1: Print the ticket scanning error rate
print('Part 1: ', ticketScanningErrorRate)

# PART 2: Remove the invalid tickets
for i in sorted(invalidTickets, reverse=True):
        del(nearbyTickets[i])

# Find the location of each field in the tickets
locationsNotFound = set(range(len(nearbyTickets[0])))

while any([field.location == -1 for field in fields]):
    for field in fields:
        if field.location == -1:
            possibleLocations = []
            for location in locationsNotFound:
                locationAvailable = True
                for ticket in nearbyTickets:
                    if not field.withinLimits(ticket[location]):
                        locationAvailable = False

                if locationAvailable:
                    possibleLocations.append(location)

            if len(possibleLocations) == 1:
                field.location = possibleLocations[0]
                locationsNotFound.remove(possibleLocations[0])

# Multiply the departure fields from my ticket together
myTicket = [int(num) for num in input[22].split(',')]
product = 1

for field in fields[:6]:
    product *= myTicket[field.location]

print('Part 2: ', product)