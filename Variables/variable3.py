# Assign Multiple Values

x,y,z = "Apple", "Ball", "Cat" # Assigning multiple variables in single line 
print(x)
print(y)
print(z)

# Assigning same value to multiple variables in one line:
a=b=c =" Abc"
print(a)
print(b)
print(c)


# UNPACK A Collection

# If you have a collection of values in a list,tuple etc.
#Python allows you to extract the value into variables . this is called unpacking
# unpacking a list

fruits = ["apple","Ball","cat"]
ab,bc,cd = fruits
print(ab)
print(bc)
print(cd)

"""
OUT PUT variables

print()
"""
abc = "Pramish is learning python"
print(abc)

# In the print() function, you can output multiple variables, separated by a comma:
apple =" Python"
Ball = " is"
cat= " Awesome"
print(apple, Ball, cat)
print(apple+Ball+cat)     # joins all the character present in the variables provided with + sign
number1=5
number2=10 
print(number1+number2) # adds the values of number1 and number2 and gives 15 as output

# + operator doesn't adds a string and an integer as it throws error
"""
a = 5
b ="apple"
print(a+ b) is wrong apporach to use + operator
"""
# print(apple+ number1) # this code throws error
print(number2,Ball) # this one will work as multiple values can be printed in same line of code

