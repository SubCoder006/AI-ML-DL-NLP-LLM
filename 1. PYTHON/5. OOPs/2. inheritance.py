
### A car composition example using inheritance
### car - base class and tesla - derived class
# class Car:
#     def __init__(self,body_type,colour,fuel):
#         self.body_type = body_type
#         self.colour = colour
#         self.fuel = fuel
        
# class Tesla(Car):
#     def __init__(self, body_type, colour, fuel, model, battery_capacity):
#         Car.__init__(self, body_type, colour, fuel)
#         self.model = model
#         self.battery_capacity = battery_capacity
        
#     def carInfo(self):
#         print(f"Model: {self.model}")
#         print(f"Body Type: {self.body_type}")
#         print(f"Colour: {self.colour}")
#         print(f"Fuel: {self.fuel}")
#         print(f"Battery Capacity: {self.battery_capacity} kWh")
        
### creating an object of Tesla class
# tesla1 = Tesla("Sedan", "Red", "Electric", "Model S", 120)
# tesla1.carInfo()


### creating multiple base classes and one derived class
### for understanding multiple inheritance
class Engine:
    def __init__(self,engine_type,horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower
        
    def engineInfo(self):
        print(f"Engine Type: {self.engine_type}")
        print(f"Horsepower: {self.horsepower} HP")

class wheels:
    def __init__(self,wheel_type,number_of_wheels):
        self.wheel_type = wheel_type
        self.number_of_wheels = number_of_wheels
        
    def wheelInfo(self):
        print(f"Wheel Type: {self.wheel_type}")
        print(f"Number of Wheels: {self.number_of_wheels}")
        
class body:
    def __init__(self,body_type,colour):
        self.body_type = body_type
        self.colour = colour
        
    def bodyInfo(self):
        print(f"Body Type: {self.body_type}")
        print(f"Colour: {self.colour}")
        
class Car(Engine,wheels,body):
    def __init__(self, engine_type, horsepower, wheel_type, number_of_wheels, body_type, colour,company):
        Engine.__init__(self, engine_type, horsepower)
        wheels.__init__(self, wheel_type, number_of_wheels)
        body.__init__(self, body_type, colour)
        self.company = company
        
    def carInfo(self):
        print(f"Company: {self.company}")
        self.engineInfo()
        self.wheelInfo()
        self.bodyInfo()
        
### creating an object of Car class
car1 = Car("V8", 450, "Alloy", 4, "SUV", "Black", "Ford")
car1.carInfo()
