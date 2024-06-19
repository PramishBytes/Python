# Global Variable

"""
Variables that are created outside of a function are known as global variables
GLobal variables can be used by everyone, both inside of function and outside
"""

x =" Pramish"
def myFunc():
    print("The  name of our hero is : " +x)

myFunc()

# create a variable inside a funciton, with the same name as the global

x = "awesome"
def myFunc():
    x= "fantastic"
    print("python is " +x)

myFunc()
print ("Python is " +x)



# Global Keyword
"""
When we create a variable inside a function, the variable becomes local, and can only be used insde the function.
To create a global variable inside a function, you can use the global keyword.
"""
def myFunc():
    global x
    x ="Pramish"
myFunc()
print("Hero no 1: " +x)


# to change the value of x
y= "awesome"
def myFunc():
    global y
    y ="cool"

myFunc()
print("pramish is " + y)
