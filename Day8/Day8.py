# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

#Game console class
class GameConsole:
    def __init__(self, programStrings):
        self.program = [re.findall('[^\s]+', programString) for programString in programStrings]
        self.instRanCntr = [0]*len(self.program)
        self.accumulator = 0
        self.instPtr = 0
        self.running = False

    def runProgram(self, accumulator=0, start=0):
        self.instRanCntr = [0]*len(self.program)
        self.accumulator = accumulator
        self.instPtr = start
        self.running = True

        while self.running:
            self._execInst()

        print('Program stopped at instruction nr ', self.instPtr, ' (', self.program[self.instPtr], ') with accumulator ', self.accumulator)

    def _execInst(self):
        if self.instRanCntr[self.instPtr] > 0:
            self.running = False
            print('Exception: infinite loop detected!')

        else:
            self.instRanCntr[self.instPtr] += 1

            if self.program[self.instPtr][0] == 'acc':
                self.accumulator += int(self.program[self.instPtr][1])
                self.instPtr += 1
            
            elif self.program[self.instPtr][0] == 'jmp':
                self.instPtr += int(self.program[self.instPtr][1])
            
            elif self.program[self.instPtr][0] == 'nop':
                self.instPtr += 1


# Create the computer and load the program
gameConsole = GameConsole(input)

# PART 1: Run the program
gameConsole.runProgram()