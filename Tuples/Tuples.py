#PYTHON - TUPLES

# Use tuples when you need an immutable, fixed collection of items.
#Use lists when you need a mutable, dynamic collection of items.
mytuple =("apple","banana","cherry")

r"""
Tuple

-> Tuples are used to store multiple items in a single variable.
-> Tuple is one of the 4 built-in data types in Python to store collection of data, the other 3 are List,Set, and Dictionary, all with different qualities and usage.
-> A tuple is a collection which is ordered and unchangeable.
-> Tuples are written with round brackets.
"""

thistuple = ("apple","banana","cherry")
print(thistuple)

#OUTPUT: ('apple', 'banana', 'cherry')

#TUPLE ITEMS
r"""
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0],the second item has index[1] etc.
"""

#ORDERED
r"""
When we say tuples are ordered,
it means that the items have a defined order, and the order will not change.
"""
#UNORDERED
r"""
When we say that tuple are ordered, it means that the items have a defined
order, and that order will not change.
"""

#UNCHANGEABLE
"""
Tuples are unchangeable, meaning that we cannot change, add or remove
items after the tuple has been created.
"""

#ALLOW DUPLICATION
" Since tuples are indexed, they can have items with the same value"

thistuple =("apple","banana","cherry","apple","cherry")
print(thistuple)

#OUTPUT: ('apple', 'banana', 'cherry', 'apple', 'cherry')

#TUPLE LENGTH -> len()
" To determine how many items a tuple has, use the len() function:"

thistuple = ("apple","banana","cherry")
print(len(thistuple))

#OUTPUT: 3


#Create Tuple with one item
#To create a tuple with only one item, you have to add a comma after the item,otherwise Python will not recognize it as a tuple

thistuple=("apple",)
print(type(thistuple))   #OUTPUT: <class 'tuple'>

#Not a tuple
thistuple= ("apple")
print(type(thistuple))   #OUTPUT: <class 'str'>

#Tuple Items -Data Types

#Tuple items can be any data tupe:
tuple1=("apple","banana","cherry")
tuple2= (1,2,3,4,5,6,7)
tuple3= (True,False,True,False)
print(type(tuple1),type(tuple2),type(tuple3))

#OUTPUT: <class 'tuple'> <class 'tuple'> <class 'tuple'>


# A tuple can contain different data types
tuple1=("abc",34,True,40,"male")
print(tuple1)

#OUTPUT: ('abc', 34, True, 40, 'male')

# The tuple() Constructor

#It is also possible to use the tuple() constructor to make a tuple.

thistuple=tuple(("apple","banana","cherry")) # note the double round-brackets
print(thistuple)

r"""
Python Collection (Arrays)

There are 4 collection data types in the python programming language:
-> List is a collection which is ordered and changeable. Allows duplicate members.
-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered and unchangable*, and unindexed. No duplice members.
-> Dictionary is a collection which is oredered ** and changeable.No duplicate members.
"""



























