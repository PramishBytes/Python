# Python - Sort Lists

r"""
Sort List Alphanumerically -> sort()


List objects have a sort() method that will sort the list alphanumerically,ascending, by defaul:

Example: Sort the list alphabetically: 

"""
thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

# OUTPUT: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Example: Sort list numerically:

thislist = [100,50,65,63,23]
thislist.sort()
print(thislist)

#OUTPUT: [23, 50, 63, 65, 100]

# SORT DESCENDING
# to sort descending, use the keyword argument "reverse = True" :

# Example: Sort the descending : 
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True) ##
print(thislist)

#OUTPUT: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# sort the list descending
thislist = [1,2,3,4,5,6,7,8,9]
thislist.sort(reverse= True)
print(thislist)

#OUTPUT: [9, 8, 7, 6, 5, 4, 3, 2, 1]

r"""
CUSTOMIZE SORT FUNCTION

You can customize your own function by using the keyword argument "key = finction". ##
The function will return a number that will be used to sort the list(the lowest number first):

Example: Sort the list based on how close the number is to 50:

"""
def myFunc(n):
    return abs(n-50)
thislist= [100,50,65,82,23]
thislist.sort(key = myFunc)
print(thislist)

#OUTPUT: [50, 65, 23, 82, 100]
    

#CASE INSENSITIVE SORT
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist  =["banana","Orange","kiwi","Cherry"]
thislist.sort()
print(thislist)


# OUTPUT: ['Cherry', 'Orange', 'banana', 'kiwi']


# Perform a case-sensitive sort of the list:
thislist =["banana","Orange","kiwi","cherry"]
thislist.sort(key = str.lower)
print(thislist)

#OUTPUT: ['banana', 'cherry', 'kiwi', 'Orange']

#REVERSE ORDER -> reverse()

#Reverse the order of the list items:
thislist=["banana","Orange","kiwi","cherry"]
thislist.reverse()
print(thislist)


#OUTPUT: ['cherry', 'kiwi', 'Orange', 'banana']
























































































