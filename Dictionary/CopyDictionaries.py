# PYTHON -> COPY DICTIONARIES

#Copy a Dictionary
"""
You cannot copy a dictionary simply by typing dict2 = dict1, because:
dict2 will only be reference to dict1, and change made in dict1 will automatically
also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy()

"""
thisdict ={
    "brand":"Ford",
    "model": "Mustang",
    "year":2024
    }
mydict = thisdict.copy()
print(mydict)

#OUTPUT: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}

#dict()

mydict = dict(thisdict)
print(mydict)


#OUTPUT: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024}
