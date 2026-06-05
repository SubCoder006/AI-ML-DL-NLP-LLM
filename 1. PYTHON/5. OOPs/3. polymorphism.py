### this is for understanding the concept of polymorphism in OOPs
### Polymorphism is the ability of an object to take on many forms. 
### It allows us to use a single interface to represent different types of objects.
### It is achieved through method overriding and abstract base classes (ABCs).

### Method Overriding: It is a feature that allows a subclass to provide a specific implementation 
### of a method that is already defined in its superclass.

class Animal:       ## this is the superclass
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):   ## this is the subclass that inherits from Animal class
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
### creating objects of Dog and Cat class
dog1 = Dog()
cat1 = Cat()
### calling the sound method for both objects
dog1.sound()  # Output: Dog barks
cat1.sound()  # Output: Cat meows

### ABCs - Abstract Base Classes
### An abstract base class is a class that cannot be instantiated and is meant to be subclassed.
### It can contain abstract methods that must be implemented by the subclasses.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("This is an abstract method for calculating area")
    
    @abstractmethod
    def perimeter(self):
        print("This is an abstract method for calculating perimeter")
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    
### creating an object of Rectangle class
rect1 = Rectangle(5, 3)
print(f"Area of rectangle: {rect1.area()}")  # Output: Area of rectangle: 15
print(f"Perimeter of rectangle: {rect1.perimeter()}")  # Output: Perimeter of rectangle: 16


### Polymorphism has it own advantages and disadvantages.
### Advantages of Polymorphism:
### 1. It allows us to use a single interface to represent different types of objects.
### 2. It promotes code reusability and flexibility.
### 3. It makes the code more maintainable and easier to extend.
### Disadvantages of Polymorphism:
### 1. It can lead to confusion if not used properly.
### 2. It can make the code more complex and harder to understand.
