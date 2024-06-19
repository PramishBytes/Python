#Python- Format - Strings

# String Format -> format()
"""
We cannot add strings like numbers
As
age = 36
txt = "My name is Pramish, I am " + age
print(txt)

 gives error as strings and numbers couldn't be added
 """

"""
Therefore we use
format() method
"""

# F-Strings
"""
F-String is preferred way of formatting strings.
To specify a string as an f-string,simply put f in front of the string literal,
and add curly brackets {} as
placeholders for variables and other operations
"""

age = 22
txt = f"My name is pramish, I am {age}"
print(txt)   #Output: My name is pramish, I am 22

#PLACEHOLDER AND MODIFIERS


price = 59
txt = f"the price is {price} rupees"
print(txt)  # Output : the price is 59 rupees

# a placeholdercan include a modifier to format the value
# A modifier is included by adding a colon ":" followed by a legal formatting type, like .2f which means fixed point number with 2 decimals


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)       # Output: The price is 59.00 dollars

# A place holder can contain Python code, like math operations:

# Example: Perform a math operation in the placeholder, and return the result

txt= f"The price is  {20*59} dollars"
print(txt)  # The price is 1180 dollars






















 
