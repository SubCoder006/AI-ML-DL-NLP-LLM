### this is a ducumentation of magic methods in python
### Magic methods in Python, also known as dunder methods (short for "double underscore"), are special methods 
# that have a specific meaning and behavior in Python. They are used to define the behavior of objects when 
# certain operations are performed on them. Magic methods are defined with double underscores at the beginning 
# and end of their names.

### Some common magic methods in Python include:
# 1. `__init__` → Initializes object when created (constructor).
# 2. `__str__` → Returns user-friendly string representation.
# 3. `__repr__` → Returns official/debug string (ideally recreatable).
# 4. `__add__` → Defines behavior of `+` operator.
# 5. `__len__` → Returns length using `len()`.
# 6. `__getitem__` → Access element using `obj[key]`.
# 7. `__setitem__` → Set element using `obj[key] = value`.
# 8. `__delitem__` → Delete element using `del obj[key]`.
# 9. `__call__` → Allows object to be called like a function.
# 10. `__eq__` → Defines `==` comparison.
# 11. `__ne__` → Defines `!=` comparison.
# 12. `__lt__` → Defines `<` comparison.
# 13. `__le__` → Defines `<=` comparison.
# 14. `__gt__` → Defines `>` comparison.
# 15. `__ge__` → Defines `>=` comparison.

### Here a code example to demonstrate the use of some magic methods in Python:
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
    
#     def __add__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         return NotImplemented

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1)          # Output: Point(2, 3)
# print(p2)          # Output: Point(4, 5)
# p3 = p1 + p2
# print(p3)          # Output: Point(6, 8)

### example using comparison operators(__eq__, __ne__, __lt__, __le__, __gt__, __ge__)
### Operator Overloading - allows us to define custom behavior for operators when they are used with instances of a class.
### In this example, we will create a `Point` class that represents a point in 2D space and overloads the comparison 
###  operators to compare points based on their distance from the origin (0, 0).
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, Point):
            return not self.__eq__(other)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) <= (other.x**2 + other.y**2)
        return NotImplemented
    
    def __gt__(self, other):  
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) >= (other.x**2 + other.y**2)
        return NotImplemented
    
p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1,p2,sep=' ,')          ## other - an instance of Point class         
print(f"{p1} == {p2}? {p1 == p2}")  # p1.__eq__(p2) will return False because the x and y values of p1 and p2 are different.
print(f"{p1} != {p2}? {p1 != p2}")  # p1.__ne__(p2)
print(f"{p1} < {p2}? {p1 < p2}")   # p1.__lt__(p2)   # Output: True
print(f"{p1} <= {p2}? {p1 <= p2}")  # p1.__le__(p2)  # Output: True
print(f"{p1} > {p2}? {p1 > p2}")   # p1.__gt__(p2)   # Output: False
print(f"{p1} >= {p2}? {p1 >= p2}")  # p1.__ge__(p2)  # Output: False
