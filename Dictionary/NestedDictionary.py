#PYTHON -> NESTED DICTIONARY

myfamily={
    "child1":{
        "name":"Email",
        "year":2001
        },
    "child2":{
        "name":"Pramish",
        "year":2024
        },
    "child3":{
        "name":"Pasu",
        "year":2006
        },
    }
print(myfamily)

"""
Output:
{'child1': {'name': 'Email', 'year': 2001}, 'child2': {'name': 'Pramish', 'year': 2024}, 'child3': {'name': 'Pasu', 'year': 2006}}
"""

#Create 3 dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Pramish",
  "year" : 2004
}
child2 = {
  "name" : "Pasu",
  "year" : 2007
}
child3 = {
  "name" : "Manish",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#OUTPUT: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#ACCESS ITEM IN NESTED DICTIONARIES

print(myfamily["child2"]["name"])

#OUTPUT : Pasu



#LOOP THROUGH NESTED DICTIONARIES -> use item() method like this:

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+':',obj[y])
        

#OUTPUT:
        """year: 2007
child3
name: Manish
year: 2011
"""






















































































