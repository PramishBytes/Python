#PYTHON FOR LOOPS

r"""

A for loop is used for iterating over a sequence(that is either a list, a tuple,a dictionary, a set, or a string).

This is less like for keyword in other programming languages, and works more like an iterator method as found in other object-oriented programming languages
With the for loop we can execute a set of statements, once for each item in a list,tuple,set,etc.


"""
fruits=["appel","banana","cherry"]
for x in fruits:
    print(x)


#Looping through string
# Even strings are iterable objects, they contain a sequence of characters:

for x in "Banana":
    print(x)


#The break statement

#With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)

#The continue statement
    #With the continue statement we can stop the current iteration of the loop, and continue with the next:

# The range() function
"""
The loop through a set of code a specified number of items, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and ends at a specified number.
"""
for x in range(7):
    print(x)

# The range() function defaults to 0 as a string value, however it is possible to specify the starting value by adding a parameter: range(2,6), which means values from 2 to 6 (but not including 6):

for x in range(2,6):
    print(x)
    
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2,30,3):

for x in range(3,30,3):
    print(x)

"""
OUTPUT:
3
6
9
12
15
18
21
24
27

"""

# Else in for loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(7):
    print(x)

else:
    print("Finally finished")
    

# The else block will not be executed if the loop is stopped by a break statement
for x in range(7):
    if x ==3: break
    print(x)

else:
    print("finally finished")
    

#Nested Loops

"""
A nested loop is a loop inside a loop.
The 'inner loop' will be executed one time for each iteration of the "outer loop"

"""

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for s in adj:
    for y in fruits:
        print(x,y)

#The pass statement
#For loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0,1,2]:
    pass






























































