# Import modules
import os
import re

# Read input
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, 'input.txt'), 'r') 
input = inputFile.read().splitlines()

# Game console class
class GameConsole:
    def __init__(self, programStrings):
        self.program = [re.findall('[^\s]+', programString) for programString in programStrings]
        self.instRanCntr = [0]*len(self.program)
        self.accumulator = 0
        self.instPtr = 0
        self.running = False
        self.exitCode = 0

    def runProgram(self, accumulator=0, start=0):
        self.instRanCntr = [0]*len(self.program)
        self.accumulator = accumulator
        self.instPtr = start
        self.running = True
        self.exitCode = 0

        while self.running:
            self._execInst()

        print('Program stopped at instruction nr ', self.instPtr, ' with accumulator ', self.accumulator, ' and exit code ', self.exitCode)

        return self.exitCode

    def _execInst(self):
        # Check if instuction pointer is outside limits
        if self.instPtr < 0 or self.instPtr >= len(self.program):
            self.running = False
            print('Exception: instruction pointer out of range!')
            self.exitCode = -1

        # Check if infinite loop is detected
        elif self.instRanCntr[self.instPtr] > 0:
            self.running = False
            print('Exception: infinite loop detected!')
            self.exitCode = -1

        # Execute the instruction
        else:
            self.instRanCntr[self.instPtr] += 1

            if self.program[self.instPtr][0] == 'acc':
                self.accumulator += int(self.program[self.instPtr][1])
                self.instPtr += 1
            
            elif self.program[self.instPtr][0] == 'jmp':
                self.instPtr += int(self.program[self.instPtr][1])
            
            elif self.program[self.instPtr][0] == 'nop':
                self.instPtr += 1

        # Check if program has terminated correctly
        if self.instPtr == len(self.program):
            self.running = False
            print('Program terminated correctly')
            self.exitCode = 1

# Create the computer and load the program
gameConsole = GameConsole(input)

# PART 1: Run the program
gameConsole.runProgram()

print('Part 1: ', gameConsole.accumulator)

# PART 2: Edit the program by trial and error until it returns exit code 1
accumulatorAtEnd = 0
for i in range(len(gameConsole.program)):
    if gameConsole.program[i][0] == 'jmp':
        gameConsole.program[i][0] = 'nop'
        if gameConsole.runProgram() == 1:
            accumulatorAtEnd = gameConsole.accumulator
        
        gameConsole.program[i][0] = 'jmp'

    elif gameConsole.program[i][0] == 'nop':
        gameConsole.program[i][0] = 'jmp'
        if gameConsole.runProgram() == 1:
            pccumulatorAtEnd = gameConsole.accumulator
        
        gameConsole.program[i][0] = 'nop'

print('Part 2: ', accumulatorAtEnd)