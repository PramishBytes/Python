#PYTHON CREATE NEW AND WRITE FILE

#Create a New File
"""
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create- will create a file,returns an error if the file exist

"a" - Append - will create a file if the specified file does not exit

"w" - Write - will create a file if the specified file does not exist
"""

f = open("myfile.txt","x") #-> creats the files 
##f = open("myfile.txt","w") -> Now it throws error as myfile.txt is already created


# Write to an Existing File

"""
To write to an Existing File like myfile.txt

"a" - Append - will append to the end of the file

"w" - Write- will overwrite any exisitng content

"""
f= open("myfile.txt","a")
f.write("This file is now written")
f.close()


f = open("myfile.txt","r")
print(f.read())

#Output: This file is now writtenThis file is now written










































