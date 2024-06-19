class User:
    
  def __init__(user, name, age):
    user.name = name
    user.age = age
    
  def printData(user,name,age):
      print(user.name)
      print(user.age)

for i in range(5):
    
    var1= input("Enter Name: ")
    var2 = input("Enter Age: ")

for i in range(5):
    p1 = User(var1,var2)
    p1.printData(var1,var2)    

