import unittest
import sys
import StringIO
from minidc import minidc


class test_minidc(unittest.TestCase):
    #test push_number with valid domain logic
    def test_push_number_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push number 5 on the stack
        calc.push_number(5)
        #check to make sure the stack has length 1
        self.assertEqual(len(calc.nums), 1)
        #check to make sure the (only) number on the stack is 5
        self.assertEqual(calc.nums.pop(), 5)

    #test add with valid domain logic
    def test_add_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 3 onto the stack
        calc.push_number(3)
        #push a 5 onto the stack
        calc.push_number(5)
        #add the two numbers together
        calc.add()
        #check to make sure the stack has length 1
        self.assertEqual(len(calc.nums), 1)
        #check to make sure the value on the stack is 8
        self.assertEqual(calc.nums.pop(), 8)

    #test subtract with valid domain logic
    def test_subtract_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 5 onto the stack
        calc.push_number(5)
        #push a 3 onto the stack
        calc.push_number(3)
        #subtract the second number from the other
        calc.subtract()
        #check to make sure the stack has length 1
        self.assertEqual(len(calc.nums), 1)
        #check to make sure the value on the stack is 2
        self.assertEqual(calc.nums.pop(), 2)

    #test multiply with valid domain logic
    def test_multiply_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 5 onto the stack
        calc.push_number(5)
        #push a 3 onto the stack
        calc.push_number(3)
        #multiply the numbers together
        calc.multiply()
        #check to make sure the stack has length 1
        self.assertEqual(len(calc.nums), 1)
        #check to make sure the value on the stack is 15
        self.assertEqual(calc.nums.pop(), 15)

    #test divide with valid domain logic
    def test_divide_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 15 onto the stack
        calc.push_number(15)
        #push a 3 onto the stack
        calc.push_number(3)
        #divide the numbers
        calc.divide()
        #make sure the stack has length 1
        self.assertEqual(len(calc.nums), 1)
        #make sure value on stack is 5
        self.assertEqual(calc.nums.pop(), 5)

    #test the p command with valid domain logic
    def test_command_p_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 4 onto the stack
        calc.push_number(4)
        #redirect stdout to something we can read
        stdout_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stdout = out

        try:
            #run the p command
            calc.command_p()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stdout = stdout_temp
        #assert that the stack length hasn't changed
        self.assertEqual(len(calc.nums), 1)
        #assert that the value printed is the values pushed
        self.assertEqual(printed, "4\n")

    #test the n command with valid domain logic
    def test_command_n_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a 10 onto the stack
        calc.push_number(10)
        #redirect stdout to something we can read
        stdout_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stdout = out

        try:
            #run the n command
            calc.command_n()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stdout = stdout_temp
        #assert that the stack length has decremented
        self.assertEqual(len(calc.nums), 0)
        #assert that the value printed is the values pushed
        self.assertEqual(printed, "10\n")

    #test the f command with valid domain logic
    def test_command_f_domain_correct(self):
        #create a calculator
        calc = minidc()
        #push a bunch of numbers onto the stack
        calc.push_number(10)
        calc.push_number(5)
        calc.push_number(3)
        #redirect stdout to something we can read
        stdout_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stdout = out

        try:
            #run the f command
            calc.command_f()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stdout = stdout_temp
        #assert that the stack length hasn't changed
        self.assertEqual(len(calc.nums), 3)
        #assert that the values printed are the values pushed
        self.assertEqual(printed, "3 5 10 \n")

    #test the execute_line command with valid domain logic
    #numbers, negative numbers and arithmetic operations
    def test_execute_line_domain_correct_1(self):
        #create a calculator
        calc = minidc()
        #execute a line
        calc.execute_line('_5 3 4 6 1 + * - /')
        #check to make sure there is only one number on the stack
        self.assertEqual(len(calc.nums), 1)
        #check to make sure the value is 0.2
        self.assertEqual(calc.nums.pop(), 0.2)

    #tests to make sure command_f, command_p and command_n are processed properly
    def test_execute_line_domain_correct_2(self):
        #create a calculator
        calc = minidc()
        #redirect stdout to something we can read
        stdout_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stdout = out

        try:
            #run a command (including command_f, command_p and command_n
            calc.execute_line('5.2 _3 f n p')
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stdout = stdout_temp
        self.assertEqual(printed, '-3 5.2 \n-3\n5.2\n')
        self.assertEqual(len(calc.nums), 1)

    #test the add function with just 1 value on the stack
    def test_add_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #push 4 onto the stack
        calc.push_number(4)
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the add command (with only 1 value)
            calc.add()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(len(calc.nums), 1)
        self.assertEqual(printed, 'Error: not enough values to add\n')

    #test the subtract function with just 1 value on the stack
    def test_subtract_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #push 4 onto the stack
        calc.push_number(4)
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the subtract command (with only 1 value)
            calc.subtract()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(len(calc.nums), 1)
        self.assertEqual(printed, 'Error: not enough values to subtract\n')

    #test the multiply function with just 1 value on the stack
    def test_multiply_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #push 4 onto the stack
        calc.push_number(4)
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the multiply command (with only 1 value)
            calc.multiply()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(len(calc.nums), 1)
        self.assertEqual(printed, 'Error: not enough values to multiply\n')

    #test the divide function with just 1 value on the stack
    def test_divide_domain_incorrect_1(self):
        #create a calculator
        calc = minidc()
        #push 4 onto the stack
        calc.push_number(4)
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the divide command (with only 1 value)
            calc.divide()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(len(calc.nums), 1)
        self.assertEqual(printed, 'Error: not enough values to divide\n')

    #test the divide function dividing by zero
    def test_divide_domain_incorrect_2(self):
        #create a calculator
        calc = minidc()
        #push 4 onto the stack
        calc.push_number(4)
        #push 0 onto the stack
        calc.push_number(0)
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the divide command (with only 1 value)
            calc.divide()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(printed, 'Error: divide by 0\n')

    #test the command_p function empty stack
    def test_command_p_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the divide command (with only 1 value)
            calc.command_p()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(printed, 'Error: empty stack\n')

    #test the command_n function empty stack
    def test_command_n_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the divide command (with only 1 value)
            calc.command_n()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(printed, 'Error: empty stack\n')

    #test the command_f function empty stack
    def test_command_f_domain_incorrect(self):
        #create a calculator
        calc = minidc()
        #redirect stderr to something we can read
        stderr_temp = sys.stdout
        out = StringIO.StringIO()
        sys.stderr = out

        try:
            #run the divide command (with only 1 value)
            calc.command_f()
            #get the value printed
            printed = out.getvalue()
        finally:
            #restore stdout
            sys.stderr = stderr_temp
        self.assertEqual(printed, 'Error: empty stack\n')


unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(test_minidc))