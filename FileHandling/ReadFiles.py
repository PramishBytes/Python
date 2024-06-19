#Python File Open

#Opent a File on the server

"""
Assume we have the following file,located in the same folder as Python:


demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purpose
Have a fine day!
"""

# TO open the file, use the built-in open() function
#The open() function returns a file object, which has a read() method for reading the content of the file:

f= open("demofile.txt")
print(f.read())

"""
OUTPUT:

Hello! Welcome to demofile.txt
This file is for testing purpose
Have a fine day!

"""

#If the file is located in a different location, you will have to specify the file path,like this:
"""
f = open("home/pramiz/Documents/Python/demofile.txt", "r")
print(f.read())
"""
# Read Only Parts of the file

#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f= open("demofile.txt","r")
print(f.read(5))

#Read Lines
#You can return one line by using the readline() method:

f= open("demofile.txt","r")
print(f.readline())


#OUPUT: Hello! Welcome to demofile.txt



#By calling readline() two times, you can read the first lines:
f= open("demofile.txt","r")
print(f.readline())
print(f.readline())



"""
OUTPUT:
Hello! Welcome to demofile.txt

This file is for testing purpose

"""

#By looping through the lines of the file, you can read the whole file, line by line:

f= open("demofile.txt","r")
for x in f:
    print(x)



"""
OUTPUT:
Hello! Welcome to demofile.txt

This file is for testing purpose

Have a fine day!

"""

#Close Files
#It is good practice to always close the file when you are done with it

f =open("demofile.txt","r")
print(f.readline())
f.close()




















































































































































































