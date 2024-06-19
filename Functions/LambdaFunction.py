#PYTHON LAMBDA

r"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

# Syntax: lambda arguments : expression

x = lambda a: a+10
print(x(5))

#OUTPUT: 15

#Lambda function can take any number of arguments:

x = lambda a,b: a*b
print(x(5,6))

#OUTPUT: 30

#Summarize argument a,b and c and return the result:

x = lambda a,b,c : a+b+c
print(x(2,3,4))

#OUTPUT: 9

# WHY USE LAMBDA FUNCTION?

"""
 The power of lambda is better shown when you use them as an anonymous function inside another function.

 Say you have a function definition that takes one argument, and the argument will be multiplied with an unknown number:
 
"""
def myfunc(n):
    return lambda a : a*n

#Use the function definition to make a function that always doubles the number you send in :

def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)
print(mydoubler(11))

#OUTPUT: 22


def myfunc(n):
    return lambda a: a*n

fun1 = myfunc(3)
print(fun1(3))

#OUTPUT: 9

def myfunc(n):
    return lambda a : a*20

fun1 = myfunc(3)
fun2 = myfunc(4)

print(fun1(3))
print(fun2(4))


"""
OUTPUT:
60
80
"""












































































































































































