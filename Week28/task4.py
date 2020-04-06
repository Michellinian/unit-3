# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include a simple test function to test the class methods by instantiating an object.

class String:
    def __init__(self, string):
        self.string = string
        self.getString()
        self.printString()

    def getString(self):
        # How to get string input from console?
        print(self.string)


    def printString(self):
        # How to make string all upper case?
        print(self.string.upper())

a = String("uppercase")


