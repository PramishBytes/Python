# Pyhton -> Delete File

#Delete a File

# To delete a file, you must import OS module, and run its os.remove() function:

import os
os.remove("myfile.txt")

#Check if file exits, then delete it:

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")

else:
    print("The file does not exist")
    

#OUTPUT: The file does not exist

#Delete Folder
"""
To delete an entire folder,use the os.rmdir() method

remove the folder "myfolder":

import os
os.rmdir("myfolder")
"""
