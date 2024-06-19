#PYTHON - TUPLE METHODS

# count() -> Returns the number of times a specified value occurs in a tuple
# index() -> Searches the tuple for a specified value and return the position of where it was found


# count() method
thistuple = (1,2,3,4,5,6,7,8,9,0)
x= thistuple.count(5)
print(x)

#Definition and Usage

#The count() method returns the number of times a specified value appers in the tuple

#Syntax: tuple.count(value)



#index() method

thistuple = (1,2,3,4,5,6,7,8,9)
x= thistuple.index(8)
print(x)

"""
Definition and Usage

The index() method finds the first occurence of the specified value.

The index() method raises an exception if the value is not found
"""

#SYNTAX: tuple.index(value)
