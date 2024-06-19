#PYTHON -> if...else

r"""
Python Conditions and if statements

Python supports the usual logical condition from mathematics:

-> Equals: a==b
-> Not Equals: a!= b
-> Less than: a<b
-> Less than or equal to : a<b
-> Greater than : a>b
-> Greater than or equal to : a>=b

These conditions can be used in several ways,most commonly in "if statements" and loops.

"""

# An "if statement" is written by using the if keyword

a= 44
b= 200
if b>a:
    print("b is greater than a")

#OUTPUT: b is greater than a



#Elif

# The elif keyword is Python;s way of saying "if the previous conditions were not true, then try this condition:

a= 33
b= 33
if b>a:
    print("b is greater than a")

elif a==b:
    print("a and b are equal")


#Else
#The else keyword catches anything which isn't caught by the preceding conditions.

a= 200
b=33

if b>a:
    print("b is greater than a")

elif a==b :
    print("a and b are equal")
else:
    print("a is greater than b")

#Short Hand if

if a>b: print("a is greater than b")

#Short Hand If...Else
#If you have only one statement to execute, one for if, and one for else,you can put it all on the same line:
a= 2
b = 22
print("A") if a>b else print("B")


# You can also have multiple else statements on the same line:

a= 33
b=33
print("A") if a>b else print("=") if a==b else print("B")

# AND -> The and keyword is a logical operator, and is used to combine conditional statements:

a=22
b=33
c=55
if a>b and c>a:
    print("Both condition are True")


# Or -> The or keyword is a logical operator, and is used to combine conditional statements:

a=22
b=33
c=55
if a>b or a>c:
    print("At least one of the conditions is True")

#NOT -> The not keyword is a logical operator, and is used to reverse the result of the conditional statement

a=22
b=44
if not a>b:
    print("a is NOT greater than b")

#NESTED IF

x=23

if x>10:
    print("Above 10")
    if x>20:
        print("And also above 20!")

    else:
        print("but not above 20")
        



# The pass Statement

a = 33
b = 300
if b>a:
    pass



































































































