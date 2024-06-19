# PYTHON-> Loop Tuples

#LOOP THROUGH A TUPLE
#Using for loop
thistuple=('apple','ball','cat')
for x in thistuple:
    print(x)

"""
apple
ball
cat
"""

#LOOP THORUGH THE INDEX NUMBERS

r"""
YOu can also loop through the tuple items by referring to their number.

Use the 'range()' and 'len()' function to create a suitable iterable.
"""

thistuple = ("apple","ball","cat")
for i in range(len(thistuple)):
    print(thistuple[i])

"""
apple
ball
cat
"""


# USING WHILE LOOP
r"""
You can loop through the tuple items by using a while loop
Use the len() function to determine the length of the tuple, then start at 0
and loop your way through the tuple items by referring to their indexes.

Remeber to increase the index by 1 after each iteration.
"""

thistuple = ("apple","banana","cherry")
i=0
while i < len(thistuple):
    print(thistuple[i])
    i=i+1

"""
apple
banana
cherry
"""




































































