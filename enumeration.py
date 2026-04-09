r""""
Enumeration() in Python

enumerate() function in Python is used to loop over an iterable and
get both the index and the element at the same time. 

It returns an enumerate object that produces pairs in the 
form (index, element). This removes the need to manually maintain 
a counter variable during iteration.

"""

# Syntax: enumerate(iterable, start = 0)
#Parameters:
# iterable: sequence or collection to iterate over.
#start(optional): starting value of the index. Default is 0

#Retrun: Retruns an enumerate object that generates (index. elecment) pairs.



'''
Example: This code shows how enumerate() provides both index
and value while iterating over a list.
'''

pramish = ["Python", "C", "C++"]
for i,v in enumerate(pramish):
    print(i,v)


'''
Output: 
0 Python
1 C
2 C++
'''