r'''

Keyword Arguments
When calling a function with optional parameters, 
you can explicitly specify which parameter you're providing a value for using keyword arguments. 
For instance, greet(name="David", greeting="Salutations") clarifies that "Salutations" is intended for the greeting parameter.

Variable Number of Arguments (*args and **kwargs) 
Python allows you to define functions that accept a variable number of arguments.
You can use *args to collect positional arguments into a tuple and **kwargs to collect keyword arguments into a dictionary.

'''

def flexible_function(*args, **kwargs):
    print("Positional arguments: ",args)
    print("Keyword arguments: ",kwargs)


flexible_function(1,2,3, name = "Pramish", age = 25)
