# Python -> UPDATE TUPLES
r"""
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds.

"""
#CHANGE TUPLE VALUES
"""
Once a tuple is created change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple inta a list, chage the list, and convert the list back into a tuple.
"""

# Convert the tuple into a list to be able to change it:
x=("apple","banana","cherry")
y= list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#OUTPUT: ('apple', 'kiwi', 'cherry')


#ADD ITEMS

r"""
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
"""
#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple","banana","cherry")
y= list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#OUTPUT: ('apple','banana','cherry','orange')

#2. Add tuple to tuple. You are allowed to add tuples to tuples, so if you want to add item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple=("apple","banana","cherry")
y=("orange",)
thistuple +=y
print(thistuple)

# OUTPUT: ('apple', 'banana', 'cherry', 'orange')

#REMOVE ITEMS
r"""
Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we
used  for changing and adding tuple items: 
"""

#EXAMPLE:
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

#OUTPUT: ('banana', 'cherry')

# OR you can delete the tuple completely:

#Example : The 'del' keyword can delete the tuple completely:
thistuple = ("apple","banana","cherry")
del thistuple
print(thistuple) # this will raise an error because the tuple no longer exists


r"""
Traceback (most recent call last):
  File "/usr/lib/python3.11/idlelib/run.py", line 579, in runcode
    exec(code, self.locals)
  File "/home/pramiz/Documents/Python/Tuples/UpdateTuple.py", line 67, in <module>
    print(thistuple) # this will raise an error because the tuple no longer exists
          ^^^^^^^^^
NameError: name 'thistuple' is not defined
"""




























































