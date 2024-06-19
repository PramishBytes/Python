#PYTHON DICTIONARIES

# Written in this way
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year" : 2024
    }

# Dictionary:

"""
Dictionaries are used to store data values in key::value pairs.

A dictionary is a collection which is ordered*, changeable and do not duplicates.
"""

# Dictionary are written with curly brackets, and have keys and values:

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year" : 2024
    }
print(thisdict)

#OUTPUT: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}


# DICTIONARY ITEMS

"""
Dictionary items are ordered,changeable,and do not allow duplication
Dictionary items are presented in key:value pairs,and can be referred to by using the key name.
"""
#Print the "brand" value of the dictionary

thisdict ={
    "brand":"Ford",
    "model":"Mustang",
    "year":2024
    }
print(thisdict["brand"])

#OUTPUT: Ford


#Ordered or Unordered?
"""
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not chage.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.


CHANGEABLE
Dictionaries are changable,meaning that we can chang,add or remove items after the dictionary has been created.


DUPLICATES NOT ALLOWED
Dictionaries cannot have two items with the same key:

Example:
"""

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":2024,
    "year":2020
    }
print(thisdict)

#OUTPUT: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Dictionary Length -> len() function
print(len(thisdict))

#OUTPUT: 3

#Dictionary Items -> Data Types

thisdict={
    "brand":"Ford",
    "electric":False,
    "year":2024,
    "colors": ["red","white","blue"]
    }


#OUTPUT: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
print(type(thisdict))

# <class 'dict'>


#The dict() Constructor
# It is possible to use the dict() constructor to make a dictionary

thisdict = dict(name ="John" , age = 35, country = "Norway")
print(thisdict)


#OUTPUT: {'name': 'John', 'age': 35, 'country': 'Norway'}

r"""
PYTHON COLLECTIONS (ARRAYS)

There are 4 collection data types in the python programming language:

-> List is a collection which is ordered, and changeable. Allows duplicate members.
-> TUple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-> Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""






































































