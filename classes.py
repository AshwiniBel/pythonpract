"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""

class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input('Enter the String: ')

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
