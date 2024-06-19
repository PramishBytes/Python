# Python Numbers
"""
There are three numeric types in python :
-> int
-> float
-> complex 
"""
x= 1   # int
y=3.8  # float
z=1j  # complex

# Int
"""
Int or integer,
is a whole number,
poisitive or negative, without decimals, of unlimited lenght.
"""

#Example
x=1
y=3567876809876867986587
z= -384923879879

print(type(x))
print(type(y))
print(type(z))

#Float

"""
Float, or "floating number" is a number,
positive or negative,
containing one or more decimals.
"""
x= 1.10
y= 1.0
z= -98709.908
print(type(x),type(y),type(z))

# Float can be scientific numbers with an "e" to indicate the power of 10

# Example:
x= 35e3
y = 12E4
z= -84.78e100
print(type(x),type(y),type(z))


# Complex
# Complex numbers are written with a "j" as the imaginary part

x= 3+5j
y=5j
z= -10j
print(type(x),type(y),type(z))

#Type Conversion


"""
You can convert
one type to another with
the int(), float(), and complex() methods
"""

x= 1
y=2.7
z= 1j

a= float(x)
b=int(y)
c= complex(x)

print(a)
print(b)
print(c)

print(type(a),type(b),type(c))










































