# Strings
"""
Strings in python are surrounded by either single quotation marks,
or double quotation marks

'hello' is as same as "hello"
you can display a string lateral with the print() function
"""

print("hello")

# Assign String to a variable

a= "hello"
print(a)

# Multiline Strings
a= """ this is
a multi line string
writting method in
python """

print(a)

# Strings as arrays
a= "hello, world"
print(a[1])


#Looping through a string

# Since strings are arrays, we can loop through the characters in a string, with a for loop


for x in "banana":
    print(x)

# String length
# to get the length of a string, use the len() function

a= "Hello Pramish"
print(len(a))

# Check String
# to check a certain phrase or character is present in a string, we can use the keyword "in"

txt = " The best thing in life are free"
print ("free" in txt) # True

# Use it in an "if" statement

# print only if "free" is present

if "free" in txt:
    print("Yes, free is present")


# check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in"

print("expensive" not in txt) # output: True


# Use it in "if" statement

# Print only if "expensive" id NOT present:

if "expensive" not in txt:
    print("No, 'expensive' is NOT present")































