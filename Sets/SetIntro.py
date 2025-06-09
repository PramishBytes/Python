#PYTHON SETS
r"""
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Pyton used to Store collections of data, the other 3 are LIST,TUPLE, AND DICTIONARY, all with different qualities and usage.
A set is a collection which is unordered, inchangable*, and unindexed.
"""

#Note: Set items are unchangable, but you can remove items and add new items.

thisset= {"apple","banana","cherry"}
print(thisset)

#SET ITEMS
#Set items are unordered, unchangeable, and do not allow duplicate values.

#UNORDERED
"""
Unordered means that the items in a set do not have a defined order.
Set item are unchanable, meaning that we cannot change the items after the set has been created.
"""

#UNCHANEABLE
#Set items are unchangable, meaning that we cannot change the items after the set has been created.

#Duplicaes NOT allowed
#Sets cannot have two items with the same value.

thisset = {"apple","banana","cherry","apple"}
print(thisset)

#OUTPUT: {'banana', 'cherry', 'apple'}

#NOTE: The values True and 1 are considered the same values in sets, and are treated as duplicates:

#Example:
thisset= {"apple","banana","cherry",True,1,2}
print(thisset)

#OUTPUT: {True, 2, 'banana', 'cherry', 'apple'}


#NOTE: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple","banana","cherry",False,True,0}
print(thisset)

#OUTPUT: {False, True, 'cherry', 'apple', 'banana'}

#GET THE LENGTH OF A SET
#To determine how many items a set has, use the len() function

thisset = {"apple","banana","cherry"}
print(len(thisset))

#SET ITEMS - DATA TYPES
set1={"apple","banana","cherr"}
set2= {1,2,3,4,5,6,8,9,0}
set3 = {True,False,True,False}

#A set can contain different data types:
#Example: A set with strings,integers and boolean values:
set1={"abc",34,True,40,"male"}
print(set1)


#type() -> From python perspective, sets are defined as object with the data type 'set':
# <class 'set'>
myset={"apple","banana","cherry"}
print(type(myset))


# The set() Constructor
#It is also possible to use the set() constructor to make a set.
thisset = set(("apple","banana","cherry"))
print(thisset)

r"""
Python Collections (Arrays)

There are four collection data types in the python programming language:
-> List is a collection which is ordered and changeable.Allows duplicate members.
-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
-> Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""




































