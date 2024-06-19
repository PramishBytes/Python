# PYTHON CLASSES AND OBJECTS

r"""
Python is an object oriented programming language.

Almost everything in Python is an object, with ites properties and methods.

A class is like an object constructor, or a "blueprint" for creating objects.

"""
#Create a Class -> use class keyword:

class MyClass:
    x = 5

#Create Object
    # Now we can use the class named MyClass to creat objects:

p1 = MyClass()
print(p1.x)

#OUTPUT: 5


# The __init__() function

r"""
The examples above are classes and objects in their simplest form, and are not really useful in real life application .

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

"""

#EXAMPLE: Create a class name Person, use the __init__() function to assign values for name and age:


class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age


p1 = Person("pramish",56)
print(p1.name)
print(p1.age)


# NOTE : The __init__() function is called automatically every time the class is being used to create a new object.


# The __str__() function

r"""
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

Example: The string representation of an object WITH the __str__() function:

"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"{self.name}({self.age})")

p1=Person("Pramish",34)
print(p1)


#OUTPUT: Pramish(34)

#OBJECT METHODS

"""
Objects can also contain methods. Methods in objects are function that belong to the object.

Let us create a method in the Person class:

"""

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person('Pramish',24)
p1.myfunc()

#OUTPUT: Hello my name is Pramish

#NOTE : The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.



#THE SELF PARAMETER

"""
The self parameter is a refernce to the current instance of the class, and is used to access variables that belongs to the class.

If does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example:
Use the words mysillyobject and abc instead of self: 
"""

class Person:
    def __init__(mysillyobject,name,age):

        mysillyobject.name = name
        mysillyobject.age = age

    def myfun(abc):
        print("My name is " + abc.name)


pq = Person('Pramish',24)
pq.myfun() 

#OUTPUT: My name is Pramish

# MODIFY OBJECT PROPERTIES

pq.age = 20
print(pq.age)


# Delete Object Properties

   # You can delete properties on objects by using the del keyword:

del pq.age

#Delete Objects -> del keyword

del pq

# The pass Statement
## class definition cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
    pass










































































