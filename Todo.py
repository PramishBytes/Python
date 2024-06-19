tasks = []


def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list.")


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >=0 and taskToDelete <len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")

        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid input.")
        
def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")


def updateTask():
    if not tasks:
        print("There are no tasks. Add one ")

    else:
        listTasks()
        try:
            taskToUpdate = int(input("Enter the # to update: "))
            if taskToUpdate >=0 and taskToUpdate < len(tasks):
                new_task = input("Enter the new task deescription: ")
                tasks[taskToUpdate] = new_task
                print(f"Task #{taskToUpdate} has been updated to: {new_task}")
            else:
                print(f"Task #{taskToUpdate} was not found")

        except ValueError:
            print("Invalid input ")
            
        

if __name__ == "__main__" :

    print("Welcome to the to do list app:) ")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task" )
        print("2. Delete a task")
        print("3. list tasks")
        print("4. Update tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTasks()

        elif(choice == "4"):
            
            updateTask()

        elif(choice == "5"):
            break

        else:
            print("Invalid input. Please try again.")

    print("Thank You")


