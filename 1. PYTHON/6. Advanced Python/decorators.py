### Decorators - A decorator is a design pattern in Python that allows you to modify the behavior of a 
# function or method by wrapping it with additional code. It is a higher-order function that takes 
# a another function as an argument and extends its behavior without explicitly modifying it.    

# A decorator is defined using the @ symbol followed by the name of the decorator function. The
# decorator function takes a function as an argument and returns a new function that adds some
# additional behavior to the original function.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")

        result = func(*args, **kwargs)

        print("After the function is called.")
        return result

    return wrapper


@my_decorator
def profileReg(name, email, number):
    print(f"Name: {name}, Email: {email}, Number: {number}")


profileReg("Subayan", "subayan@example.com", 9874651230)  