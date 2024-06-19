# PYTHON Try Except
"""
The try block lets you test a block of code for errors

The except block lets you handle the error

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try - and except blocks.



"""


"""
Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

The exceptions can be handled using the try statement: 
"""
try:
    print(x)

except:
    print("An exception occured")


#Many Exceptions

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else is wrong")




# Else -> You can use else keyword to define a block of code to be executed if no errors were raised:

try:
    print("Hello")
except:
    print("Something went wrong")

else:
    print("Nothing went wrong")


# finally block , if specified will be executed regardless if the block raises an error or not

try:
    print(x)
except:
    print("Something went wrong")

finally:
    print("The 'try except' is finished")



# try to open and write to a file that is not writeable:

try:
    f = open("demofile.txt")
    try:
        f.write("Hello")

    except:
        print("Something went wrong when writing to the file")

    finally:
        f.close()

except:
    print("Something went wrong when opening the file")

    
"""
Raise an exception

As a Pyhton developer you can choose to throw an execption if a condition occurs.

To throw(or raise) an exception, use the raise keyword.
"""

x = -1

if x<0:
    raise Exception("Sorry, no number below zero")

"""
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

"""
x = "hello"
if not type(x) is int:
    raise TypeError('Only integers are allowed')


"""
OUTPUT OF ALL ABOVE CODE :

An exception occured
Variable x is not defined
Hello
Nothing went wrong
Something went wrong
The 'try except' is finished
Something went wrong when opening the file
Traceback (most recent call last):
  File "/usr/lib/python3.11/idlelib/run.py", line 579, in runcode
    exec(code, self.locals)
  File "/home/pramiz/Documents/Python/try_except/TryExcept.py", line 93, in <module>
    raise Exception("Sorry, no number below zero")
Exception: Sorry, no number below zero



"""


















