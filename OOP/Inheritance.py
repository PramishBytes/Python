#PYTHON INHERITANCE

"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

"""

#Create A parent Class

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)


x = Person("Pramish","Adhikari")
x.printname()

# Create a child class

## To create a class that inherits the functionailty from the anther class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

# Use the pass keyword when you do not want to add any other properties to the class.

x = Student("Pasu","Adikari")
x.printname() 

# OUTPUT : Pasu Adhikari



# ADD the __init__() Function
"""
So far we have created a child class that inherites the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).


NOTE: The __init__() function is called autonatically every time the class is being used to create a new object

"""
#Example:

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

# Now we have successfully added the __init__() function,and kept the inheritance of the parent class, and we are ready to the functionality in the __init__() funtion.

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,laname)



# Use the super() function

# Python also hava a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# ADD properties
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduateyear = 2025


p1 =Student("Pramish","Adhikari")
print(p1.graduateyear)
p1.printname()


#In the example below, the year 2025 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__()

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear =year


x = Student("Pramish","Adhkari",2024)

print(x.graduationyear)


# ADD Methods
# Add a method called welcome to the student class:

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("Pramish","Adhikari",2025)
x.welcome() 




































