# PYTHON - JOIN LISTS

#Join Two Lists

# using '+' operator

list1= ["a","b","c"]
list2= [1,2,3]
list3 = list1+list2
print(list3)

#OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1=["a","b","c"]
list2=[1,2,3]

for x in list2:
    list1.append(x)

print(list1)


#OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# Or You can use extend() method, where the purpose is to add elements from one list to another list: -> extend()

list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)

#OUTPUT: ['a', 'b', 'c', 1, 2, 3]
