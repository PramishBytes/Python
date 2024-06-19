#PYTHON -> JOIN SETS
r"""
Join Sets
There are several ways to join two or more sets in Python.
The union() and update() method joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s)
The symmetric_difference() method keeps all items Except the duplicates.

"""

#UNION -> union()
# The union() method returns a new set with all items from both sets.

set1={"a","b","c"}
set2={1,2,3}
set3 = set1.union(set2)
print(set3)

#OUTPUT: {1, 'c', 2, 'a', 3, 'b'}


#You can use '|' operator instead of union() method, and you will get the same result.

set1= {"a","b","c"}
set2={1,2,3}
set3 = set1|set2
print(set3)


#OUTPUT:{1, 2, 3, 'a', 'c', 'b'}

# JOIN MULTIPLE SETS
"""
All the joining methods and operators can be used to join multiple sets.
When using a method, just add more sets in the parenthesis, separated by commas:

"""
#Example:
set1 ={"a","b","c"}
set2 ={1,2,3}
set3 = {"John","Eleena"}
set4 = {"apple","banana","cherry"}

myset = set1.union(set2,set3,set4)
print(myset)

#OUTPUT: {'John', 1, 'c', 'a', 2, 3, 'Eleena', 'apple', 'cherry', 'banana', 'b'}


#When using the '|' operator, separate the sets with more '|' operators:


set1 ={"a","b","c"}
set2 ={1,2,3}
set3 = {"John","Eleena"}
set4 = {"apple","banana","cherry"}

myset= set1|set2|set3|set4
print(myset)

#OUTPUT: {1, 2, 3, 'Eleena', 'apple', 'a', 'c', 'b', 'banana', 'cherry', 'John'}



# JOIN A SET WITH A TUPLE
"""
The union() method allows you to join a set with other data types,like lists or tuples.

The result will be a set.
"""
x={"a","b","c"}
y=(1,2,3)

z= x.union(y)
print(z)

#OUTPUT: {'b', 1, 'a', 2, 'c', 3}

# UPDATE
"""
The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set

"""
set1={"a","b","c"}
set2={1,2,3}

set1.update(set2)
print(set1)


#OUTPUT: {'a', 1, 2, 3, 'c', 'b'}

# Both union() and update() will exclude any duplicate item.

#INTERSECTION -> intersection() method

set1={"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3= set1.intersection(set2)
print(set3)


#OUTPUT: {'apple'}


#The intersection_update() method will also keep only the duplicates, but it will change the original set instead of returning a new set.

set1= {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.intersection_update(set2)

print(set1)

#OUTPUT: {'apple'}

#The values True and 1 are considered the same value. The same goes for false and 0.

set1={"apple",1,"banana",0,"cherry"}
set2={False,"google",1,"apple",2,True}

set3 = set1.intersection(set2)
print(set3)

#OUTPUT: {False, 1, 'apple'}

#Difference
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1={"apple","banana","cherry"}
set2 ={"google","microsoft","apple"}

set3 = set1.difference(set2)

print(set3)


#OUTPUT: {'banana', 'cherry'}

# Use "-" operator instead of the difference() method, and you will get the same result

set1 ={"apple","banana","cherry"}
set2 ={"google","microsoft","apple"}

set3 = set1 - set2
print(set3)

#OUTPUT: {'cherry', 'banana'}



# THE difference_update() method to keep the items that are not present in both sets:

set1 ={"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.difference_update(set2)

print(set1)

#OUTPUT: {'banana', 'cherry'}

"""
You can use the ^ operator instead of the symmetric_differnece() method, and you will get the same result.

Example: 

"""
set1={"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1^set2
print(set3)


###OUTPUT: {'banana', 'cherry', 'microsoft', 'google'}

### symmetric_difference_update() method

set1={"apple","banana","cherry"}
set2 ={"google","microsoft","apple"}

set1.symmetric_difference_update(set2)

print(set1)

#OUTPUT: {'banana', 'microsoft', 'google', 'cherry'}













































































