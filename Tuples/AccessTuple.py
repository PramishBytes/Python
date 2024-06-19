# Python - Access Tuple Items

# ACCESS TUPLE ITEMS
"""
You can access tuple items by referring to the index number,inside square brackets:

Example:
Print the second item in tuple:
"""
thistuple = ("apple","banana","cherry")
print(thistuple[1])

#OUTPUT: banana

#NEGATIVE INDEXING

"""
Negative indexing means start from the end.

-1 refers  to the last item, -2 refers to the second last item etc.
"""

thistuple=("apple","banana","cherry")
print(thistuple[-1])

#OUTPUT: cherry


#RANGE OF THE INDEXES
r"""

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specifying items.

"""
thistuple= ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:3])

#OUTPUT : ('cherry',)

#The example returns the items from the beginning to, but NOT included "kiwi":
thistuple =("apple","banana","cherry","orange","kiwi","melon")
print(thistuple[:4])

# The example returns the items from "cherry" and to the tuple:
thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:])


# RANGE OF NEGATIVE INDEXES
#Specify negative index if you want to start the search from the end of the tuple
thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[-4:-1])

#CHECK IF ITEM EXISTS
thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the first tuple")











































