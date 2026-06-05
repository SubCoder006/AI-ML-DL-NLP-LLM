### This document is about encapsulation in python
### Encapsulation - Encapsulation is one of the fundamental principles of object-oriented programming
### (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on the 
### data into a single unit, called a class. It also restricts direct access to some of the object's components,
### which can prevent the accidental modification of data.
### In Python, encapsulation is achieved through the use of access modifiers. There are three types of access modifiers :
### 1. Public: Attributes and methods that are declared as public can be accessed from anywhere
### 2. Protected: Attributes and methods that are declared as protected can only be accessed within the class 
###               and its subclasses. In Python, we use a single underscore (_) before the attribute or method
###               name to indicate that it is protected.
### 3. Private: Attributes and methods that are declared as private can only be accessed within the class.
###             In Python, we use a double underscore (__) before the attribute or method name to indicate that it is private.

### Getters and Setters: Getters and setters are methods that allow us to access and modify the private attributes of a class.
### A getter method is used to retrieve the value of a private attribute, while a setter method is used to set the value of 
### a private attribute.

### Example of encapsulation in Python
class Person:
    def __init__(self, name):
        self.__name = name  # private attribute
        
    def get_name(self):   # getter method for name
        return self.__name
    
    def set_name(self, name):  # setter method for name
        self.__name = name
    
class Employee(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)  # calling the constructor of the base class
        self._age = age        # protected attribute
        
    def get_age(self):   # getter method for age
        return self._age
    
    def set_age(self, age):  # setter method for age
        self._age = age
