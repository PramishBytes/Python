# Data Types
"""
Built in Data Types
Variables can store data of different types, and different types can do different things
Python has following data types built in by default, in this categories:

Text type : str
Numeric type : int, float,complex
Sequence Type : list, typle, range
Mapping Type : dict
Set type : set, frozenset
Boolean Type : bool
Binary type  : bytes, bytearray, memoryview
None Type : NoneType
"""

# Getting the Data Type
"""
You can get the data type of any object by using the "type()" function
"""

x = 5
print(type(x))

# output: class <int>

# Setting the Data Types

a= "Hello"
print(type(a))  # output : class <str>

a= 20
print(type(a))  # output: class <int>

a= 20.5
print(type(a)) # output : class <float>

a = 1j
print(type(a)) # output : class <complex>

a= ["apple" ,"Ball", "cat"]
print(type(a))   # output : class <list>

a= ("apple","ball","cat")
print(type(a)) # output : class <tuple>

a= range(6)
print(type(a))  # output: class <range>

a= {"apple","ball","cat"}
print(type(a)) # output : class <set>

a= {"name":"Pramish", "age":22}
print(type(a)) # output: class <dict>

a= frozenset({"apple","ball","cat"})
print(type(a)) # output: class <forzenset>


a= True
print(type(a)) # output: class <bool>

a= b"hello"
print(type(a)) # output: class <bytes>

a= bytearray(5)
print(type(a)) # output: class <bytearray>

a= memoryview(bytes(5))
print(type(a)) # output: class <memeoryview>

a = None
print(type(a)) # output: None

# Setting Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

x= str("hello")
x= int(30)
x= float(20.3)
x= complex(1j)
x = list(("apple","ball","cat"))
x = tuple(("apple","ball","cat"))
x = range(6)
x= dict(name = "pramish",age = 22)
x= set(("apple","ball","cat"))
x= frozenset(("apple","ball","cat"))
x= bool(5)
bytes(5)
x= bytearray(4)
x= memoryview(bytes(5))


