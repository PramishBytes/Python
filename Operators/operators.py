# Python Oprators

r"""
Python divides the operators in following groups:
-> Arithmetic operators
-> Assignment operators
-. Comparison Operators
-> Logical operators
-> Identity operators
-> Membership operators
-> Bitwise operators

"""
# ARITHMETIC OERATOR 

# Addition Operator  = '+'
a = 10
b = 20
print(a+b)

# Subtraction operation = '-'

print(a-b)


# Multiplication = '*'

print(a*b)

# Division = ' / '

print(a/b)

# Modulus ' % '
print(a%b)

# Exponentiation ' ** '
print(a**b)  #10 power 20 



# // Floor Division

print (a//b)  # the floor division rounds the result down to the nearest whole number


# ASSIGNMENT OPERATORS

r"""
-> = : x=5               x=5

-> += : x+=3             x = x+3

-> -= : x-=3            x = x-3

-> /= : x/=3            x = x/3

-> %= : x%= 3           x= x%3

-> //= : x//=3           x= x//3

-> **= : x**=3           x = x**3

-> &= : x&=3             x = x &3     // BITWISE AND operator, which performs a bitwise AND operation or two integers

-> |= : x|=3            x = x | 3       

-> ^= : x^=3            x = x^3    

-> >>= : x>>=3           x = x>>3

-> <<= : x<<=3          x= x<<3

-> := : print (x:=3)     x =3
                         print(x)
"""



# COMPARISON OPERATORS

r"""
==  Equal

!=  Not Equal

>   Greater than

<   Less than

>=  Greater than or equal to

<=  Less than or equal to 

"""

# LOGICAL OPERATORS

r"""
and -> returns True if both statements are true:  x<5 and x>10

or -> returns True if one of the statements is true  x<5 or x>4

not -> reverse the result, returns False if the result is true  not(x<5 and x<10)

"""

# IDENTITY OPERATORS

r"""
is -> returns True if both varaibles are the same object   # x is y

is not -> returns True if both varaibale are not the same object  # x is not y

"""

# MEMBERSHIP OPERATORS

r"""
in -> Returns True if a sequence with specified value is present in the object : x in y

not in -> Returns True if a sequence with the specified value is present in the object

"""


# BITWISE OPERATORS

r"""
& -> AND : Sets each bit to 1 if both bits are 1
| -> OR : Sets each bit to 1 if one of two bits is 1
^ -> XOR: Sets each bit to 1 if only one of two bits is 1
~ -> NOT : Inverts all the bits
<< -> Zero fill left shift : Shifts left by pushing zeros in from the right and let the leftmost bit fall off
>> -> Signed right shift: Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""


# OPERATOR PRECEDENCE
r"""
Operator precedence describes the order in which operations are performed.

The precedence order is described in the table below, starting with the highest precedence at the top:

() -> Parenthesis

** -> Exponentiation

+x,-x,~x -> Unary plus ,unary minus, and bitwise NOT

*,/,//,% -> Multiplication, division, floor division, and modulus

+,- -> Addition and subtraction

<< ,>> -> Bitwise left and right shifts

& -< Bitwise AND

^ -> Bitwise XOR

| -> Bitwise OR

==,!=,>,>=,<,<=,is, is not, in, not in -> Comparisions, identity, and membership operators

not -> Logical NOT

and -> AND

or -> OR
"""













































































































