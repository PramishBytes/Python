# Python - List Comprehension

r"""
List Comprehension offers a shorter syntax when you want to create a new list
based on the values of an exiting list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with
the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside: 
"""
#Example:
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


r"""
output:

['apple', 'banana', 'mango']


Explaination:
Initialization:

fruits is a list containing the strings: ["apple", "banana", "cherry", "kiwi", "mango"].
newlist is an empty list initialized to store the results.
Iteration:

The for loop iterates over each element in the fruits list.
During each iteration, the variable x takes on the value of the current element from fruits.
Condition Check:

Inside the loop, the if statement checks if the character "a" is present in the string x.
If "a" is found in x, the append method adds x to the newlist.
Result:

The print(newlist) statement outputs the newlist after the loop completes.
Type of x:

x is a string type. In each iteration, it holds one of the strings from the fruits list.

"""


# with list comprehension you can do all that with only one line of code:

#Example:

fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)


r"""
THE SYNTAX

newlist= [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
"""

# CONDITION
"""
The condition is like filter that only accepts the items that valuate to True.

Example:
Only accept items that are not apple.
"""
newlist = [x for x in fruits if x!="apple"]
print(newlist)

#OUTPUT: ['banana', 'cherry', 'kiwi', 'mango']

r"""
The condition if x!="apple" will return True for all elements other than "apple", making the new list contain all fruits
except "apple".

The condition is optional and can be omitted:

Example:
With no if statement 
"""
newlist=[x for x in fruits]
print(newlist)



#ITERABLE

r"""
The iterable can be any iterable object, like a list, tuple,set etc.
Example:
You can use the range() function to create an iterable:

"""
newlist = [x for x in range(10)]
print(newlist)

#OUTPUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Same example,but with condition:
#Accept only numbers lower than 5:

newlist=[x for x in range(10) if x<5]
print(newlist)

#OUTPUT : [0, 1, 2, 3, 4]

# Expression : The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

#Example:

newlist= [x.upper() for x in fruits]
print(newlist)

#OUTPUT: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#You can set the outcome to whatever you like:

#Example: Set all values in the new list to 'hello'

newlist= ['hello' for x in fruits]
print(newlist)


# OUTPUT: ['hello', 'hello', 'hello', 'hello', 'hello']


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

#Example: Return "orange" instead of "banana":

newlist=[x if x!= "banana" else "orange" for x in fruits]
print(newlist)


#OUTPUT: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Return the item if it is not banana, if it is banana return orange


















































