# Python - Modify Strings

# Python has a set of built-in methods that you can use on strings

# Upper Case -> upper()

# Example
"""
the uppet() method
returns the string
in upper case:
"""
a = "hello world"
print(a.upper())

#Lower Case -> lower()
"""
the lower()
method returns the string in lower case
"""

print(a.lower())

#Remove White Space -> strip()
print(a.strip())

 # Replace String -> replace()

# the replce() method replaces a string with another string
print(a.replace("h" ,"j"))


# Split String -> split()

# The split() method splits the string into substrings if it finds instances of the separator

print(a.split(",")) # returns ['hello','world']
