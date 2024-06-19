#Python Polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

#FUNCTION POLYMORPHISM

#String -> len() returns the number of characters:

x = 'hello world'
print(len(x))

#Tuple
mytuple = ("apple","banana","cherry")
print(len(mytuple))


#Dictionary
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2023
    }
print(len(thisdict))


# Class Polymorphism
"""
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane and they all have a method called move():

"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747")

for x in (car1,boat1,plane1):
    x.move() 



"""
OUTPUT:
Drive
Sail
fly
"""

# INHERITANCE CLASS POLYMORPHISM
"""
What about classes with child classes with the same name? Can we use polymorphism there?

Yes, if we use the example above and make a parent class called Vehicle , and make Car,Boat,Plane, child classes of Vehicle, the child classes inherits the vehicle
method, but  can override them:

"""
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail")

class Plane(Vehicle):
    def move(self):
        print("fly")

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 =Plane("Boeing","747")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
    
"""
OUTPUT;
Ford
Mustang
Move
Ibiza
Touring 20
sail
Boeing
747
fly
"""

r"""
Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

##Because of polymorphism we can execute the same method for all classes.
"""











































