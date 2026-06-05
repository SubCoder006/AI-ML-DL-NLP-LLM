### This is to understand how to create custom error handling in python 
### This are used in cases where we want to raise specific exceptions for certain conditions in our code.
### We can create custom exceptions by defining a new class that inherits from the built-in `Exception` class.
### Here is an example of how to create a custom exception for handling invalid age input:
class Error(Exception):
    """Base class for other exceptions"""
    pass

class dobError(Error):
    """Raised when the input age is less than 20 or greater than 35"""
    pass
    def __str__(self):
        return "Invalid age. Age must be between 20 and 35."

age = int(input("Enter your age: "))
try:
    if(age < 20 or age > 35 ):
        raise dobError
    else:
        print("You can give the exam.")
except dobError:
    print(dobError())
    