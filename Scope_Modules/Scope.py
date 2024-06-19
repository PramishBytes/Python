# PYTHON SCOPE
"""
A variable is only available form inside the region it is created. This is called scope.

Local Scope
A variable created inside a funtion belongs to the local scope of that function, and only can be used inside the function.

"""
def myfunc():
    x = 300
    print(x)

myfunc()


#Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)

    myinnerfunc()

myfunc()


#OUTPUT: 300

#GLOBAL SCOPE:
"""
A variable created in the main body of the python code is a global variable and belongs to the global scope.

Global variable are available from within any scope, global and local

"""

x = 300

def myfun():
    print(x)

myfunc()
print(x)


#Naming Variables

"""
If you operate with the same variable name inside and outside of a function, Pyhton will treat them as two separate variables, one available in the global scope
(Outside the function) and one available in the local scope(inside the function):

"""

x = 400
def myfunc():
    x = 300
    print(x)

myfunc()
print(x)


#OUTPUT:
# 300
# 400





# Use of global keyword and nonlocal keyword

x = 300
def myfunc():
    global x
    x =200

myfunc()
print(x)

#OUTPUT: 200




# nonlocal keyword -> Used to work with variables inside nested functions, and makes the variable belong to the outer function

def myfunc():
    x = "Pramish"
    def myfunc2():
        nonlocal x
        x = "hello"

    myfunc2()
    return x
print(myfunc())


#OUTPUT: hello 

















































































