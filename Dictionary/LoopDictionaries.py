#PYTHON -> LOOP DICTIONARY

thisdict ={
    "brand":"Ford",
    "model": "Mustang",
    "year":2024
    }


#Loop Through Dictionary

#for loop
for x in thisdict:
    print(x)
    

# Print all values in the dictionary, one by one:

for x in thisdict:
    print(thisdict[x])

# You can use the values() method

for x in thisdict.values():
    print(x)

#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
    print(x)
    

#Loop Through both keys and values, by using the items() method:

for x,y in thisdict.items():
    print(x,y)

