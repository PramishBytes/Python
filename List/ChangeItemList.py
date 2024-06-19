# PYTHON -> Change List Items

#CHANGE ITEM VALUE
#To change the value of a specific item, refer to the index number:

# Example:
#Change the second item:

thislist = ["apple","banana","cherry"]
thislist[1]= "blackcurrant"
print(thislist)

#output: ['apple', 'blackcurrant', 'cherry']

#CHANGE A RANGE OF ITEM VALUES

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
#Example:
# Change the values "banana" and "cherry" with the values "blackcurrent" and "watermelon"
thislist= ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrent","watermelon"]
print(thislist)

# OUTPUT: ['apple', 'blackcurrent', 'watermelon', 'orange', 'kiwi', 'mango']

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example:
# Change the second value by replacing it with two new values:

thislist=["apple","banana","cherry"]
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)

#OUTPUT: ['apple', 'blackcurrant', 'watermelon', 'cherry']
r"""
In Python, when you use slice assignment on a list, the slice notation start:stop specifies a range of indices from start to stop, but not including stop. This is why index 1 is replaced, but index 2 is not.

Here's a breakdown:

thislist[1:2]:

start is 1.
stop is 2.
This selects the sublist starting at index 1 up to (but not including) index 2, which in this case is ["banana"].
When you assign ["blackcurrant", "watermelon"] to this slice, you are replacing the elements in the selected sublist with the new elements. This operation effectively removes the element at index 1 ("banana") and inserts "blackcurrant" and "watermelon" in its place.

The list transformation can be visualized as follows:

Original list: ["apple", "banana", "cherry"]
Slice selected: thislist[1:2] which is ["banana"]
Replace ["banana"] with ["blackcurrant", "watermelon"]
The list then becomes: ["apple", "blackcurrant", "watermelon", "cherry"].

So, index 1 ("banana") is replaced, but index 2 ("cherry") is not affected by this operation.


"""

# If you insert less items than you replace,the new items will be inserted where you specified, and the remaining items will move accordingly

#Example:
# Change the second and third value by replacing it with one value:
thislist = ["apple","banana","cherry"]
thislist[1:3]= ["watermelon"]
print(thislist)

#OUTPUT: ['apple', 'watermelon']

r"""
Explanation:

thislist[1:3] selects the slice from index 1 to 3, which includes elements at indices 1 and 2 (["banana", "cherry"]).
Assigning ["watermelon"] to this slice replaces the elements in the selected sublist.
The final list is ["apple", "watermelon"], where both "banana" and "cherry" are replaced by "watermelon".
"""

#INSERT ITEMS

#To insert a new list item,without replacing any of the existing values,we can use the 'insert()' method.

#This 'insert()' method inserts an item at the specified index:

#Example: Insert "watermelon" as the third item:

thislist =["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

#OUTPUT : ['apple', 'banana', 'watermelon', 'cherry']



























