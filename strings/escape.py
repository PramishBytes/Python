# Escape Characters
"""
Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash "\" followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# txt = " We are the so-called "Vikings" from the north" 

To fix this problem, use the escape character \"

"""

# Example
txt = "We are the so-called \"Vikings\" from the north"
print(txt)  # Output: We are the so-called "Vikings" from the north

r"""
Escape Characters

Other escape characters used in Python:

Code      Result
 \'       Single Quote
 \\       Backslash
 \n       New Line
 \r       Carriage Return
 \t       Tab
 \b       Backspace
 \f       Form Feed
 \ooo     Octal value
 \xhh     Hex value
"""

txt = 'It\'s alright'
print(txt)  # Output: It's alright

txt = "This will insert one \\ (backslash)."
print(txt)  # Output: This will insert one \ (backslash).

txt = "Hello \r World"
print(txt)   # Ouptut :  World


                




















