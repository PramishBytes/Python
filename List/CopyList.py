#Python -> COPY LISTS

# COPY A LIST
r"""
You cannot copy a list simply by typing list2=list1, because list2 will obly be a referenct to list1, and change made in list1 will automatically also be made in list2

There are ways to make a copy, one way is to use the built-in List method copy().

"""

#Example:
#Make a copy of a list with the copy() method: -> variable2 = variable1.copy()

thislist=["apple","banana","cherry"]
mylist=thislist.copy()
print(mylist)

#OUTPUT: ['apple', 'banana', 'cherry']


#Another way to make a copy is to use the built-in method list()

thislist=["apple","banana","cherry"]
mylist= list(thislist)
print(mylist)

#OUTPUT: ['apple', 'banana', 'cherry']


































