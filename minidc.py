import sys
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
        #pop the first number off the stack
        num1 = self.nums.pop()
        #pop the second number off the stack
        num2 = self.nums.pop()
        #divide num2 by num1 and push the result back onto the stack
        self.nums.append(num2 / num1)

    #peeks at the top number on the stack and prints it out
    def command_p(self):
        #pop the top number off the stack
        topnum = self.nums.pop()
        #push it back onto the stack
        self.nums.append(topnum)
        #print the number to stdout
        print topnum

    #pops the top number off the stack and prints it out
    def command_n(self):
        print self.nums.pop()

    #prints the entire stack without altering it
    def command_f(self):
        for num in reversed(self.nums):
            sys.stdout.write(str(num) + ' ')
        sys.stdout.write('\n')

    def execute_line(self):
        pass

    def run(self):
        pass