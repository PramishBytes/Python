# Python Boolean
"""
Booleans represent one of two values: True or False

Boolean Values
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two anwers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
# Example
print(10>9)  # Output: True
print (10==9) # Output: False
print(10<9)   # Output : False

# When You run a condition in an if statement, Python returns True or False:

a= 200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output: b is not greater than a

# Evaluate Values and Variables

# This bool() function allows you to evaluate any value, and give you True or False in return

print(bool("Hello")) # Output: True
print(bool(15))    #Output: True

x= "Hello"
y= 15
print(bool(x)) # Output: True
print(bool(y))  #Output: True


# Most Values are True
"""
Almost any value is evaluated to True if it has some sort of content
Any string is True, except empty strings.
Any number is True, except 0
Any list, tuple,set,and dictionary are True, execpt empty ones.
"""
#Example:
bool("abl")
bool(123)
bool(["apple","ball","cat"])



# Some Values are False
r"""
There are not many values that evaluate to False, except empty values, such as (),[],{}," ",
the number 0 , and the value None
And the value False itself
evaluates to False
"""

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case to False, and that is if you have an object that is made from a class with a _len_ function that returns 0 or False:

class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Output: False

# Function can Return a Boolean

def myFunction():
    return True

print (myFunction())

# Output : True

def function():
    return True
if function():
    print("Yes")
else:
    print("NO")


# Output: Yes

# Python also has many built in function that return a boolean value,
# like the isinstance() function, which can be used to determine if an object
# is of certain data type

# Example:

x= 2000
print(isinstance(x, int))



#Output : True





















