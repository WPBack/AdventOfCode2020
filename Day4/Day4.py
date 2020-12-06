# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().split("\n\n")

# Passport class
class Passport:
    def __init__(self, passportString):
        self.byr = re.search('byr:([^\s]+)', passportString)
        self.iyr = re.search('iyr:([^\s]+)', passportString)
        self.eyr = re.search('eyr:([^\s]+)', passportString)
        self.hgt = re.search('hgt:([^\s]+)', passportString)
        self.hcl = re.search('hcl:([^\s]+)', passportString)
        self.ecl = re.search('ecl:([^\s]+)', passportString)
        self.pid = re.search('pid:([^\s]+)', passportString)
        self.cid = re.search('cid:([^\s]+)', passportString)

    def hasAllFields(self):
        return self.byr != None and self.iyr != None and self.eyr != None and self.hgt != None and self.hcl != None and self.ecl != None and self.pid != None

    def isValid(self):
        if not self.hasAllFields():
            return False
        
        byrValid = len(self.byr.group(1)) == 4 and int(self.byr.group(1)) >= 1920 and int(self.byr.group(1)) <= 2002
        iyrValid = len(self.iyr.group(1)) == 4 and int(self.iyr.group(1)) >= 2010 and int(self.iyr.group(1)) <= 2020
        eyrValid = len(self.eyr.group(1)) == 4 and int(self.eyr.group(1)) >= 2020 and int(self.eyr.group(1)) <= 2030

        hgtValue = re.search('\d+', self.hgt.group(1))
        hgtUnit  = re.search('\D+', self.hgt.group(1))
        if hgtValue == None or hgtUnit == None:
            return False
        hgtValid = (hgtUnit.group(0) == 'cm' and int(hgtValue.group(0)) >= 150 and int(hgtValue.group(0)) <= 193) or \
                   (hgtUnit.group(0) == 'in' and int(hgtValue.group(0)) >=  59 and int(hgtValue.group(0)) <=  76)

        hclValue = re.search('#([0-9A-Fa-f]+)', self.hcl.group(1))
        if hclValue == None:
            return False
        hclValid = len(self.hcl.group(1)) == 7 and len(hclValue.group(1)) == 6

        eclValid = self.ecl.group(1) == 'amb' or self.ecl.group(1) == 'blu' or self.ecl.group(1) == 'brn' or self.ecl.group(1) == 'gry' or self.ecl.group(1) == 'grn' or self.ecl.group(1) == 'hzl' or self.ecl.group(1) == 'oth'

        pidValue = re.search('\d+', self.pid.group(1))
        if pidValue == None:
            return False
        pidValid = len(self.pid.group(1)) == 9 and len(pidValue.group(0)) == 9
        
        return byrValid and iyrValid and eyrValid and hgtValid and hclValid and eclValid and pidValid

# Create list of passports
passports = [Passport(passportString) for passportString in input]

# PART 1: Count number of passports with all fields except cid
numHasAllFields = 0
for passport in passports:
    if passport.hasAllFields():
        numHasAllFields += 1

print('Part 1: ', numHasAllFields)


# PART 1: Count number of passports with valid data
numValid = 0
for passport in passports:
    if passport.isValid():
        numValid += 1

print('Part 2: ', numValid)