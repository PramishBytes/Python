# Python Modules
"""
What is Module?

Consider a module to be the same as a code library

A file containing a set of functions you want to include in your application

"""

"""
Create a Module

To create a module just save the code you want in a file with the file extension .py: 
"""

"""
it takes the part like import sqlite3

import Scope as Scope is made already

"""


"""
Sample example:


import mymodule
a = mymodule.person1["age"]
print(a)


Here mymodule.py is being called which contains the code;


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
"""



#Renaming a Module
"""
Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

"""
"""
Import only person1 dictionary from the module:

from mymodule import person1

print (person1["age"])

"""


#Built in modules

import platform

x = platform.system()
print(x)



#OUTPUT: Linux


















