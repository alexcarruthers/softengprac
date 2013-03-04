import sys
import re


class minidc:
    def __init__(self):
        self.nums = []

    #Takes a number and push it onto the stack so that
    #it can be stored for future computation
    def push_number(self, num):
        #push number onto the stack
        self.nums.append(num)

    #pops the top two numbers off of the stack, adds them
    #and pushes it back onto the stack
    def add(self):
        #make sure there are at least two numbers on the stack
        if len(self.nums) < 2:
            sys.stderr.write('Error: not enough values to add\n')
            raise ArithmeticError
        else:
            #pop the first number off the stack
            num1 = self.nums.pop()
            #pop the second number off the stack
            num2 = self.nums.pop()
            #add the numbers and pop the result back onto
            #the stack
            self.nums.append(num1 + num2)

    #pops the top two numbers off of the stack, subtracts one
    #from the other and pushes it back onto the stack
    def subtract(self):
        #make sure there are at least two numbers on the stack
        if len(self.nums) < 2:
            sys.stderr.write('Error: not enough values to subtract\n')
            raise ArithmeticError
        else:
            #pop the first number off the stack
            num1 = self.nums.pop()
            #pop the second number off the stack
            num2 = self.nums.pop()
            #add the numbers and pop the result back onto
            #the stack
            self.nums.append(num2 - num1)

    #pops the top two numbers off of the stack and multiplies
    #them together and pushes the result back onto the stack
    def multiply(self):
        #make sure there are at least two numbers on the stack
        if len(self.nums) < 2:
            sys.stderr.write('Error: not enough values to multiply\n')
            raise ArithmeticError
        else:
            #pop the first number off the stack
            num1 = self.nums.pop()
            #pop the second number off the stack
            num2 = self.nums.pop()
            #multiply the two numbers and push the result back
            #onto the stack
            self.nums.append(num1 * num2)

    #pops two top numbers off the stack and divides the second
    #by the first and pushes the result back onto the stack
    def divide(self):
        #make sure there are at least two numbers on the stack
        if len(self.nums) < 2:
            sys.stderr.write('Error: not enough values to divide\n')
            raise ArithmeticError
        else:
            #pop the first number off the stack
            num1 = self.nums.pop()
            if num1 == 0:
                sys.stderr.write('Error: divide by 0\n')
                raise ArithmeticError
                #pop the second number off the stack
            num2 = self.nums.pop()
            #divide num2 by num1 and push the result back onto the stack
            self.nums.append(num2 / num1)

    #peeks at the top number on the stack and prints it out
    def command_p(self):
        if len(self.nums) == 0:
            sys.stderr.write('Error: empty stack\n')
            raise Exception
            #pop the top number off the stack
        topnum = self.nums.pop()
        #push it back onto the stack
        self.nums.append(topnum)
        #print the number to stdout, stripping trailing zeroes
        print '{0:g}'.format(float(topnum))

    #pops the top number off the stack and prints it out, stripping trailing zeroes
    def command_n(self):
        if len(self.nums) == 0:
            sys.stderr.write('Error: empty stack\n')
            raise Exception
        print '{0:g}'.format(float(self.nums.pop()))

    #prints the entire stack without altering it, stripping trailing zeroes
    def command_f(self):
        if len(self.nums) == 0:
            sys.stderr.write('Error: empty stack\n')
            raise Exception
        for num in reversed(self.nums):
            sys.stdout.write('{0:g}'.format(float(num)) + ' ')
        sys.stdout.write('\n')

    # take a line of commands and execute them
    def execute_line(self, line):
        #small function to check if a string is a number (int or float)
        def is_number(s):
            try:
                float(s)
            except ValueError:
                return False
            return True

        #split the line based on the expressions that constitute numbers and commands
        splitline = filter(lambda x: x.strip(), re.split("(\s|\+|\-|\*|/|_?\d*\.?\d+|[a-zA-Z]|_\.|_)", line))
        for i in splitline:
            if i == '+':
                self.add()
            elif i == '-':
                self.subtract()
            elif i == '*':
                self.multiply()
            elif i == '/':
                self.divide()
            elif i == 'n':
                self.command_n()
            elif i == 'f':
                self.command_f()
            elif i == 'p':
                self.command_p()
            elif i[0] == '_' and is_number(i[1:]):
                self.push_number(float('-' + i[1:]))
            elif is_number(i):
                self.push_number(float(i))
            #special cases that result in 0
            elif i == '_' or i == '_.':
                self.push_number(0)
            else:
                sys.stderr.write('Error: \'' + i + '\': Not a valid operation\n')
                raise Exception

    #continually run commands until q (for quit) is entered
    def run(self, commands=sys.stdin.readline):
        sys.stdout.write('$ ')
        instruction = commands()
        while instruction != 'q\n':
            try:
                self.execute_line(instruction)
            except (ArithmeticError, Exception):
                sys.stdout.write('\n')
            sys.stdout.write('$ ')
            instruction = commands()

