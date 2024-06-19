#PYTHON -> WHILE LOOPS

#Python loops:
"""
python has two primitive loop commands:
-> while loops
-> for loops

"""

# The while loop
# With the while loop we can execute a set of statements as long as a condition is true:

i = 1
while i<10:
    print(i)
    i +=1

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1

#The break statement
# With the break statement we can stop the loop even if the while condiotion is true:

i = 1
while i<8:
    print(i)

    if i ==3:
        break

    i +=1



#The continue statement : -> With the continue statement we can stop the current itereation, and continue with the next:

i=0
while i<9:
    i+=1
    if i == 3:
        continue
    print(i)

# The else statement
#With the else statement we can run a block of code once when the condition no longer is true:

i =1
while i<8:
    print(i)
    i+=1

else:
    print("i is no longer less than 8")
    




















