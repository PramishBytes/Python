# PYTHON -> ADD SET ITEMS

#ADD ITEMS -> add()



#To add one item to a set use 'add()' method


thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

#OUTPUT: {'apple', 'cherry', 'orange', 'banana'}


#ADD SETS -> update()

thisset = {"apple","banana","cherry"}
tropical= {"pineapple","mango","papaya"}

thisset.update(tropical)
print(thisset)



#ADD ANY ITERABLE -> update
# The object in the update() method does not have to be a set, it can be any iterable object(tuple,lists,dictionaries etc).

thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]
thisset.update(mylist)
print(thisset)


#OUTPUT: {'orange', 'kiwi', 'apple', 'cherry', 'banana'}






































