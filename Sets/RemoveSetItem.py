#PYTHON -> REMOVE SET ITEMS


#Remove Item -> remove() or discard() method


#To remove an item in a set, use the remove() and discard() method.

thisset ={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#OUTPUT: {'apple', 'cherry'}

# discard()

thisset = {"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

#OUTPUT: {'apple', 'cherry'}


r"""
You cna also use the pop() method to remove an item, but this method will remove a random item,so you cannot be sure what item tha gets removed.
The return value of the pop() method is the removed item .
"""



#pop() method

thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)


#OUTPUT: {'banana', 'apple'}




#The clear() method empties the set:

thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)

#OUTPUT: set()

# del keyword will delete will delete the set completely

thisset= {"apple","banana","cherry"}
del thisset
print(thisset)


"""
OUTPUT:
Traceback (most recent call last):
  File "/usr/lib/python3.11/idlelib/run.py", line 579, in runcode
    exec(code, self.locals)
  File "/home/pramiz/Documents/Python/Sets/RemoveSetItem.py", line 48, in <module>
    print(thisset)
          ^^^^^^^
NameError: name 'thisset' is not defined
"""


















