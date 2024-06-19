print("\t\t\t\t TO-DO List\n\n\n")
 
print(" Enter a choice:\n")
print(" Choose '0' to create a todo")
print(" Choose '1' to read a todo")
print(" Choose '2' to update todo")
print(" Choose '3' to delete todo")
choice = input()
 
# Converting choice to an integer
choice = int(choice)
 
class CRUD:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
 
    def DisplayData(self,name):
    
        if self.name is not None and self.age is not None:
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
        else:
            print("No data available.")
 
user = CRUD()
 
if choice > 3 or choice < 0:
    print("Only from 0 to 3")
elif choice == 0:
    print("It's create todo list")
    
    user.name = input("Enter name: ")
    user.age = input("Enter age: ")
    user.age = int(user.age)
    
elif choice == 1:
    print("It's read todo list")
    user.DisplayData()
    
elif choice == 2:
    print("It's update todo list")
    user.name = input("Enter new name: ")
    user.age = input("Enter new age: ")
    user.age = int(user.age)
elif choice == 3:
    print("It's delete todo list")
    user.name = None
    user.age = None
    print("Todo deleted successfully.")
