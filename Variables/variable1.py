# Python variables
"""
Variables are
containers for storing data values
"""
"""

Creating Variables:
-> Python has no command for declaring a variable.
-> A variable is created the moment you first assign a value to it.
-> Variable do not need to be declared with any particular type.
"""

x=5  # X is of type integer
y="Pramish" # y is now of type string
x ="hero" # x is overwritten
print(x)
print(y)

#CASTING
""" If you want to specify
the data type of a variable,
this can be done with casting.
"""
a= str(3) # a wil be '3' (string)
b= int(3) # b will be 3(integer)
c= float(3) #c will be 3.0 (floating number)
d='abc'
"""
To know which Type
use type()
function
"""
print(type(a))
print(type(b))
print(type(x))
print(type(d))

# Single and Double Quotes
"""
single quote and
double quote both
explains that
the variable/ data type is string 
"""
first = " you are"
first = " you are"
print(first)

# Case-Semsitive
ab=10
Ab= "pramish"
# Ab will not overwrite ab
print(Ab)
print(ab)

