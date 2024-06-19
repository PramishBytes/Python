#PYTHON -> UNPACK TUPLES

#Unpack a tuple:
#When we create a tuple, we normally assign values to it. This is called 'packing' a tuple:
fruits=("apple","banana","cherry")
print(fruits)

#OUTPUT: ('apple', 'banana', 'cherry')

fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#OUTPUT:
"""
apple
banana
cherry
"""

#USING ASTERIK *

r"""
If the number of variables is less than the number of values,you can add an
'*' to the variable name and the values
will be assigned to the variable as a list:

Example: Assign the rest of the values as a list called 'red'.

"""
fruits =("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)


##Output:['cherry', 'strawberry', 'raspberry']



































