# Python Lists -> [] -> One of the 4 built in data types

mylist = ["apple","ball","cat"]

r"""
List
-> Lists are used to store multiple items in a single variable.
-> Lists are one of 4 built-in data types in Python used to store collection of data, the other 3 are Tuple,Set, and Dictionary, all with different qualities and usage.
-> Lists are created using square brackets
"""

# Example

thelists = [1,2,"hero","ball"]
print(thelists)
print(type(thelists))  # Output: <class 'list'>

# List Items
r"""
List items are ordered changeable, and allow duplicate values.

List items are indexed, the first item has index[0], the second item has index[1] etc.

"""

#ORDERED
"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change

If you add new items to a list, the new items will be placed at the end of the list.

"""

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# CHANGABLE:

# The list is changable, meaning that we can change, add, and remove items in a list after it has been created.

# ALLOWS DUPLICATES:
# Since lists are indexed, list can have items with the same value:

 #Example
thislist = ["apple","ball","cat","apple","ball"]
print(thislist)



#LIST LENGTH

# To determine how many items a list has, use the 'len()' function:

#Example

thislist= ["apple","banana","cherry"]
print(len(thislist))

#LIST ITEMS - DATA TYPES
#list can be of any data type:
#Example:
# String, int, and boolean data types:
list1 = ["apple","banana","cherry"]
list2 = [1,3,5,7,9]
list3 = [True,False,False]

# A list can contain different data types:
"""
Example:
A list with strings, integers and boolean values:
"""
list1 = ["abc",53,True,34,"male"]

#type()
# From Python perspective, list are defined as objects with the data type 'list':
# <class 'list'>

# Example:
# What is the data type of a list?
mylist = ["apple","banana","cherry"]
print(type(mylist))

# the list() CONSTRUCTOR
# It is also possible to use the list() constructor when creating a new list.

# Example:
# Using the list() constructor to make a List:

thelist = list(("apple","banana","cherry")) # note the double round-brackets
print(thislist)









# PYTHON COLLECTIONS (ARRAYS)
"""
There are 4 collection data types in the Python programming language:
-> List is a collection which is ordered and changeable. Allows duplicate members.

-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

-> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

-> Dictionary is a collection which is ordered ** and changeable. No duplicate members.

"""
























































