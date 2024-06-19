# PYTHON -> ACCESS DOCTIONARY ITEMS

#ACCESSING ITEMS
thisdict = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 2024
    }
x= thisdict["model"]
print(x)

#OUTPUT: Mustang

# get() function

x=thisdict.get("model")

#OUTPUT: Mustang

# GET KEYS -> keys()
x= thisdict.keys()
print(x)

#OUTPUT: dict_keys(['brand', 'model', 'year'])


# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
    "brand":"Ford",
    "model": "Mustang",
    "year":2024
    }
x= car.keys()
print(x)
car["color"] = "white"
print(x)

#dict_keys(['brand', 'model', 'year', 'color'])

#GET VALUES -> values() method will return a list of all the values in the dict
x= thisdict.values()
print(x)

#OUTPUT: dict_values(['Ford', 'Mustang', 2024])

x = car.items()
print(x)
car["year"] = 2020
print(x)

#OUPUT: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'white')])

car["color"] = "red"
print(x)


#OUTPUT: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'red')])

# To determine if a specified key is present in a dictionary use the in keyword:

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")



#OUTPUT: Yes, 'model' is one of the keys in the thisdict dictionary






















