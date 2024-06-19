# Python - Remove List Items

# REMOVE SPECIFIED ITEM -> remove()
# the remove() method removes the specified item.

# Example : Remove banana
thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

#OUTPUT: ['apple', 'cherry']

# If there are more than one item with the specified value, the remove() method removes that first occurrence:

#Example : remove the first occurrence of "banana"
thislist= ["apple","banana","cherry","banana","kiwi"]
thislist.remove("banana")
print(thislist)
 
#OUTPUT: ['apple', 'cherry', 'banana', 'kiwi']



# REMOVE SPECIFIED INDEX -> pop()
# the pop() method removes the specified index.

# Example: Remove the second item
thislist= ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

#OUTPUT: ['apple', 'cherry']


#If you don't specify the index, the pop() method removes the last item.
thislist= ["apple","banana","cherry"]
thislist.pop()
print(thislist)

#OUTPUT: ['apple','banana']


# DEL KEYWORD

# The 'del' keyword also remove the specified index:
#Example: Remove the first item:

thislist= ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#OUTPUT: ['banana', 'cherry']


# The del keyword can also delete the list completely

#Example: Delete the entire list:
thislist= ["apple","banana","cherry"]
del thislist


# CLEAR THE LIST -> clear()
# the clear() method empties the list
# the list still remains, but it has no content
# Example: Clear the list content
thislist= ["apple","banana","cherry"]
thislist.clear()
print(thislist)

# OUTPUT: []

















