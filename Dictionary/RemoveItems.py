#PYTHON -> REMOVE ITEMS



#Removing items -> pop()
thisdict ={
    "brand":"Ford",
    "model":"Mustang",
    "year":2025
    }
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item

thisdict ={
    "brand":"Ford",
    "model":"Mustang",
    "year":2024
    }
thisdict.popitem()
print(thisdict)

#OUTPUT: {'brand': 'Ford', 'model': 'Mustang'}

# del keyword
del thisdict["model"]
print(thisdict)

#OUTPUT: {'brand': 'Ford'}

# The clear() method

thisdict.clear()
print(thisdict)

#OUTPUT: {}
































