# Python - Access List Items

# Access Items
#List items are indexed and you can access them by referring to the index number:

# Example:

thislist=["apple","banana","cherry"]
print(thislist[1])    #OUTPUT : apple


# NEGATIVE INDEXING
r"""
Negative indexing means start from the end
-1 refers to the last item,
-2 refers to the second last item etc
"""

thislist= ["apple","banana","cherry"]
print(thislist[-1])     #OUTPUT: cherry

#Range of Indexes
r"""
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""

thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

#Note: The search will start at index 2included) and end at index 5(not included).

#OUTPUT: cherry,orange,kiwi

# This example returns the items from the beginning to, but NOT including, "kiwi"
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])

# OUTPUT: ['apple', 'banana', 'cherry', 'orange']

#By leaving out the end value, the range will go on to the end of the list:

#Example:
# This example returns the items from "cherry" to the end:

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])

#OUTPUT: ['cherry', 'orange', 'kiwi', 'melon', 'mango']


# RANGE OF NEGATIVE INDEXES

r"""
Specify negative indexes if you want to start the search fromt the end of the list:

Example:
This example returns the items from "orange"(-4) to, but NOT including "mango" (-1):

"""
thislist= ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[-4:-1])

#OUTPUT: ['orange', 'kiwi', 'melon']

# CHECK IF ITEM EXISTS

#To determine if a specified item is present in a list use the in keyword:

"""
Example
check if "apple" is present in the list:
"""
thislist= ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in this fruits list")

#OUTPUT: Yes, 'apple' is in this fruits list


























































