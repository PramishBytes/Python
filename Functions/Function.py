#Python Functions
"""
A funtion is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

"""
# Creating a Function
# In a function is defined using the def function

def my_func():
    print("Hello pramish")

my_func()


# Creating a function
# In python a function is defined using def keyword:

def my_function():
    print("Hello from a functio")

#Calling a Function:

def my_function():
    print("Hello form a function")

my_function()

#Arguments
"""
Information can be passed into function as arguments.
Arguments are specified after the function name, inside the parenthesis. You can add as many arguments as you want, just separate the into a comma.
The following example has a function with one argument(fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

"""
def my_function(fname):
    print(fname + " Adhikari")

my_function("Pramish")
my_function("Pasu")
my_function("Milan")

# Arguments are oftern shortened to args in Python documentations.

#Parameters or Arguments?
"""
The terms parameter and argument can be used for the same thing: information that are passed into a function

From a function's perspective:
A parameter is the variable listed inside the parenthesis in the funtion definition
An argument is the value that is sent to the function when it is called.
"""

#NUMBERS OF ARGUMENTS
## By default, a function must be called with the correct number of arguments. Meaning that if your function excepts2 arguments, you have to call the function with 2 arguments, not more, and not less.

def my_function(fname,lname):
    print(fname + " " + lname)

my_function("Pramish","Adhikari")


#Arbitary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function,

add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:


"""

def my_function(*kids):
    print("The youngest child is "  + kids[2])

my_function("Pramish", "Pasu","Manish")


## Keyword Arguments
"""
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""

def my_function(child3,child2,child1):
    print("The youngest child is " + child3)

my_function(child1 = "Pramish", child2 = "Pasu", child3 = "Badger")

# Arbitrary keyword Argumentsm, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Pramish",lname = "Adhikari")


r"""
Default Parameter Value

The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value: 
"""
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Nepal")
my_function("USA")
my_function("UK")

my_function()
my_function("Australia")

# PASSING A LIST AS AN ARGUMENT
"""
You can send any data types of argument to a function(string,number,list,dictionary etc) and it will be treated as the same data type inside the function.

E.g. if you send a List as an argumentm it will be a list when it reaches the function:

"""


def my_function(food):
    for x in food:
        print(x)



fruits = ["apple","banana","cherry"]
my_function(fruits)


"""
OUTPUT:
apple
banana
cherry

"""


#Returns Values

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(4))
print(my_function(9))


# The Pass Statement
# function definition cannot be empty, but if you for some reason have a function definition with no content , put in the pass statement to avoid getting an error.

def myfunction():
    pass



#POSITIONAL - ONLY ARGUMENTS
"""
You can specify that a function can have ONLY positional argumentsm or ONLY keyword arguments.
To specify that a function can have only positional arguments, add, / after the arguments:

"""

def my_function(x,/):
    print(x)

my_function(3)

#OUTPUT: 3

#Keyword - Only Arguments

def my_function(*,x):
    print(x)

my_function(x=3)

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(x):
    print(x)

my_function(3)


# Combine Positional-Only and keyword-Only
"""
You can combine the two argument types in the same function
Any argument before the /, are positional-only, and any argument after the *, are keyword-only

"""

def my_function(a,b,/,*,c,d):
    print(a+b+c+d)

my_function(5,6,c=7,d=8)
    


#OUTPUT: 26

r"""
Recursion :
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function whicn never terminatesm or one that uses excess amounts of memory or processor
power. However, when written correctly recursion can be a very efficient and mathematically- elegant approach to programming.

In this example. tri_recursion() is a function that we have defined to call itseld("recuse"). We use the k variable as the data, which decrements(-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e when it is 0).


"""

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)

    else:
        result = 0

    return result

print("\n\n Recursion Example Results")
tri_recursion(6)


#OUTPUT:
"""

 Recursion Example Results
1
3
6
10
15
21

"""






























































































